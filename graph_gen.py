import csv
import yaml
import os

import networkx as nx


def generate(storage):
    def pack_row(module_id, class_type, floor, rack, cell, side):
        row_struct = [
            "_".join([str(module_id), "A", str(floor), str(rack), str(cell), side]),
            None,
            True,
            class_type,
            floor,
            rack,
            cell,
            side,
        ]
        return row_struct

    BASE_DIR = os.path.dirname(__file__)
    db_predata = [["id", "cont_id", "empty", "class_type", "floor", "rack", "cell", "side"]]

    modules = storage["modules"]

    g = nx.DiGraph()
    storage_struct = []

    for module_id, module in enumerate(modules, 1):
        # add lifts "<module_id>_<type>_<cross_link>_<cell>"
        for cross in module["lift"]["cs_link"]:
            # for cell in range(1, module["lift"]["cell"] + 1):
            n = g.add_node(
                "_".join([str(module_id), "L", "1", str(cross), "1"]),
                module_id=module_id,
                type="L",
                cross=cross,
                x=module["cross"]["weight"] * (cross - 1),
                y=-module["lift"]["weight"],
                z=0.0
            )

        # add CS and racks "<module_id>_<type>_<floor>_<cross/rack>_<cell>"
        for floor in range(1, module["floor"]["count"] + 1):
            for cross in range(1, module["cross"]["count"] + 1):
                n = g.add_node(
                    "_".join([str(module_id), "CS", str(floor), str(cross), "1"]),
                    module_id=module_id,
                    type="CS",
                    floor=floor,
                    cross=cross,
                    cell=1,
                    x=module["cross"]["weight"] * (cross - 1),
                    y=0.0,
                    z=module["floor"]["weight"] * (floor - 1),
                )

                if int(cross) > 1:
                    # to
                    e = g.add_edge(
                        "_".join([str(module_id), "CS", str(floor), str(cross), "1"]), # source
                        "_".join([str(module_id), "CS", str(floor), str(cross-1), "1"]), # target
                        type="CS",
                        dir="left",
                        csN=1,
                        weight=module["cross"]["weight"],
                        # e._directed = True
                    )

                    # back
                    e = g.add_edge(
                        "_".join([str(module_id), "CS", str(floor), str(int(cross)-1), "1"]), # source
                        "_".join([str(module_id), "CS", str(floor), str(cross), "1"]), # target
                        type="CS",
                        dir="right",
                        csN=1,
                        weight=module["cross"]["weight"],
                        # e._directed = True
                    )

                if cross in module["lift"]["cs_link"]:
                    # to
                    e = g.add_edge(
                        "_".join([str(module_id), "CS", str(floor), str(cross), "1"]),
                        "_".join([str(module_id), "L", "1", str(cross), "1"]),
                        type="CS",
                        dir="backward",
                        csN=1,
                        weight=module["lift"]["weight"],
                        # e._directed = True
                    )

                    # back
                    e = g.add_edge(
                        "_".join([str(module_id), "L", "1", str(cross), "1"]),
                        "_".join([str(module_id), "CS", str(floor), str(cross), "1"]),
                        type="CS",
                        dir="forward",
                        csN=1,
                        weight=module["lift"]["weight"],
                        # e._directed = True
                    )

                # Recharge point
                if cross == module["recharge_point"]["cross"] and floor == module["recharge_point"]["floor"]:
                    r = g.add_node(
                        "_".join([str(module_id), "R", str(floor), str(cross), "1"]),
                        module_id=module_id,
                        type="R",
                        floor=floor,
                        cross=cross,
                        x=module["cross"]["weight"] * (cross - 1),
                        y=-module["recharge_point"]["weight"],
                        z=module["floor"]["weight"] * (floor - 1)
                    )

                    # to
                    e = g.add_edge(
                        "_".join([str(module_id), "CS", str(floor), str(cross), "1"]),
                        "_".join([str(module_id), "R", str(floor), str(cross), "1"]),
                        type="CS",
                        dir="backward",
                        csN=1,
                        weight=module["recharge_point"]["weight"],
                        # e._directed = True
                    )

                    # back
                    e = g.add_edge(
                        "_".join([str(module_id), "R", str(floor), str(cross), "1"]),
                        "_".join([str(module_id), "CS", str(floor), str(cross), "1"]),
                        type="CS",
                        dir="forward",
                        csN=1,
                        weight=module["recharge_point"]["weight"],
                        # e._directed = True
                    )

                # Enter point
                if cross == module["enter_point"]["cross"] and floor == module["enter_point"]["floor"]:
                    e = g.add_node(
                        "_".join([str(module_id), "E", str(floor), str(cross), "1"]),
                        module_id=module_id,
                        type="E",
                        floor=floor,
                        cross=cross,
                        x=module["cross"]["weight"] * (cross - 1),
                        y=-module["recharge_point"]["weight"],
                        z=module["floor"]["weight"] * (floor - 1),
                    )

                    # to
                    e = g.add_edge(
                        "_".join([str(module_id), "CS", str(floor), str(cross), "1"]),
                        "_".join([str(module_id), "E", str(floor), str(cross), "1"]),
                        type="CS",
                        dir="backward",
                        csN=1,
                        weight=module["enter_point"]["weight"],
                        # e._directed = True
                    )

                    # back
                    e = g.add_edge(
                        "_".join([str(module_id), "E", str(floor), str(cross), "1"]),
                        "_".join([str(module_id), "CS", str(floor), str(cross), "1"]),
                        type="CS",
                        dir="forward",
                        csN=1,
                        weight=module["enter_point"]["weight"],
                        # e._directed = True
                    )

            for rack in module["rack"]["cs_link"]:
                for cell in range(1, module["section"]["count"] * module["section"]["cells_per_section"] + 1):
                    # if "aisle" in module and module["aisle"]["rack"] == [] or rack in module["aisle"]["racks"]:
                    #     cell_type = "A"
                    # elif "shoot" in module and module["shoot"]["rack"] == [] or rack in module["shoot"]["rack"]:
                    #     cell_type = "S"
                    # else:
                    #     cell_type = "C"
                    n = g.add_node(
                        "_".join([str(module_id), "A", str(floor), str(rack), str(cell)]),
                        module_id=module_id,
                        type="A",
                        floor=floor,
                        rack=rack,
                        cell=cell,
                        x=module["cross"]["weight"] * (rack - 1),
                        y=module["cell"]["weight"] * (cell - 1) + \
                            (cell - 1) // module["section"]["cells_per_section"] * module["section"]["section_gap"] + \
                            module["rack"]["weight"],
                        z=module["floor"]["weight"] * (floor - 1),
                    )

                    # add DB predata
                    if cell <= module["class"]["A"]:
                        class_type = "A"
                    elif cell <= module["class"]["B"]:
                        class_type = "B"
                    else:
                        class_type = "C"
                    db_predata.append(pack_row(module_id, class_type, floor, rack, cell, "L"))
                    db_predata.append(pack_row(module_id, class_type, floor, rack, cell, "R"))

                    # add edges
                    if cell == 1:
                        # to
                        e = g.add_edge(
                            "_".join([str(module_id), "A", str(floor), str(rack), str(cell)]),
                            "_".join([str(module_id), "CS", str(floor), str(rack), "1"]),
                            type="CS",
                            dir="backward",
                            csN=1,
                            weight=module["rack"]["weight"],
                            # e._directed = True
                        )

                        # back
                        e = g.add_edge(
                            "_".join([str(module_id), "CS", str(floor), str(rack), "1"]),
                            "_".join([str(module_id), "A", str(floor), str(rack), str(cell)]),
                            type="A",
                            inverse=False,
                            holeN=1,
                            weight=module["rack"]["weight"],
                            # e._directed = True
                        )

                    if cell > 1:
                        # to
                        e = g.add_edge(
                            "_".join([str(module_id), "A", str(floor), str(rack), str(cell)]),
                            "_".join([str(module_id), "A", str(floor), str(rack), str(cell-1)]),
                            type="A",
                            inverse=True,
                            holeN=1,
                            weight=module["cell"]["weight"] + module["section"]["section_gap"] if (cell - 1) % module["section"]["cells_per_section"] == 0 else module["cell"]["weight"],
                            # e._directed = True
                        )

                        # back
                        e = g.add_edge(
                            "_".join([str(module_id), "A", str(floor), str(rack), str(cell-1)]),
                            "_".join([str(module_id), "A", str(floor), str(rack), str(cell)]),
                            type="A",
                            inverse=False,
                            holeN=1,
                            weight=module["cell"]["weight"] + module["section"]["section_gap"] if (cell - 1) % module["section"]["cells_per_section"] == 0 else module["cell"]["weight"],
                            # e._directed = True
                        )

    # write graph
    nx.write_graphml_lxml(g, "./output/temp_storagenx.graphml")

    # write db predata
    with open(os.path.join(BASE_DIR, 'output', 'temp_db_predata.csv'), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(db_predata)

    return g, db_predata
