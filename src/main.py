#!/usr/bin/env python

import datetime
import os
import runpy

skipped_tasks = [""]


def get_task(final_task: str) -> str:
    """Ask to correctly choose the task to solve."""
    n = int(final_task)
    range_task = [str(x) for x in range(1, n + 1)]
    while True:
        task_string = input(f"Please, choose task [1--{n}]: ")
        if task_string in range_task:
            if task_string in skipped_tasks:
                print(
                    f"    Sorry, tasks {skipped_tasks} have been skipped for the moment: solutions will be added shortly."
                )
            else:
                break
        else:
            print(
                f"    Please, enter only an integer number between 1 and {n}."
            )
    return f"{int(task_string):03d}"


def main() -> None:
    """Determine how many tasks are solved and run the right solver."""
    last_solved_task = (
        max([f for f in os.listdir("src/") if f.startswith("euler_")])
        .split(".py")[0]
        .split("euler_")[1]
    )
    starting_time = datetime.datetime.now()

    runpy.run_path(
        path_name="src/euler_" + get_task(last_solved_task) + ".py",
        run_name="__main__",
    )

    print("Running time: ", datetime.datetime.now() - starting_time)


if __name__ == "__main__":
    main()
