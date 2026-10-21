
from dataclasses import dataclass

@dataclass
class Task:
    name: str
    execution: int
    period: int


@dataclass
class Job:
    name: str
    release: int
    deadline: int
    remaining: int
    period: int
    order: int
    completion: int = None
    missed: bool = False


# Common example for all three algorithms
tasks = [
    Task("A", execution=1, period=4),
    Task("B", execution=2, period=5),
    Task("C", execution=1, period=8),
]

SIMULATION_TIME = 20


def simulate(algorithm):
    jobs = []
    gantt = []
    order = 0
    busy_time = 0

    for t in range(SIMULATION_TIME):
        # Release new jobs
        for task in tasks:
            if t % task.period == 0:
                jobs.append(Job(
                    name=task.name,
                    release=t,
                    deadline=t + task.period,
                    remaining=task.execution,
                    period=task.period,
                    order=order
                ))
                order += 1

        # Mark unfinished jobs whose deadlines have passed
        for job in jobs:
            if (
                job.remaining > 0
                and not job.missed
                and job.deadline <= t
            ):
                job.missed = True

        # Find ready jobs
        ready = [
            job for job in jobs
            if job.release <= t
            and job.remaining > 0
        ]

        selected = None

        if ready:
            if algorithm == "LIFO":
                # Most recently released job first
                selected = max(
                    ready,
                    key=lambda j: (j.release, j.order)
                )

            elif algorithm == "RM":
                # Shortest task period has highest priority
                selected = min(
                    ready,
                    key=lambda j: (j.period, j.order)
                )

            elif algorithm == "EDF":
                # Earliest absolute deadline first
                selected = min(
                    ready,
                    key=lambda j: (j.deadline, j.order)
                )

        # Execute the selected job for one time unit
        if selected:
            selected.remaining -= 1
            busy_time += 1

            if selected.remaining == 0:
                selected.completion = t + 1

            gantt.append((t, t + 1, selected.name))
        else:
            gantt.append((t, t + 1, "IDLE"))

    # Count jobs that missed deadlines, including unfinished jobs
    for job in jobs:
        if job.remaining > 0 and job.deadline <= SIMULATION_TIME:
            job.missed = True

    completed = [
        job for job in jobs
        if job.completion is not None
    ]

    missed = [job for job in jobs if job.missed]

    # Merge consecutive intervals with the same running task
    merged = []
    for start, end, name in gantt:
        if merged and merged[-1][2] == name:
            merged[-1] = (merged[-1][0], end, name)
        else:
            merged.append((start, end, name))

    print(f"\n===== {algorithm} =====")
    print("Gantt chart:")
    print(" | ".join(
        f"{start}-{end}: {name}"
        for start, end, name in merged
    ))

    print(f"Total jobs released: {len(jobs)}")
    print(f"Completed jobs: {len(completed)}")
    print(f"Missed deadlines: {len(missed)}")
    print(f"CPU utilization: {busy_time / SIMULATION_TIME * 100:.1f}%")

    if completed:
        avg_turnaround = sum(
            job.completion - job.release
            for job in completed
        ) / len(completed)

        print(f"Average turnaround time: {avg_turnaround:.2f}")

    print("Missed job names:", [
        job.name + f"(release={job.release})"
        for job in missed
    ])


# Run all algorithms on the same task set
for algorithm in ["LIFO", "RM", "EDF"]:
    simulate(algorithm)
