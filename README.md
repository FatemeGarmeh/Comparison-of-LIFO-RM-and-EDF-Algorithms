Comparison of LIFO, RM, and EDF Scheduling Algorithms 1. Introduction 

Scheduling algorithms play an important role in operating systems and computer systems. They determine the order in which tasks or processes are executed by the CPU. Choosing an appropriate scheduling algorithm can improve system performance, resource utilization, response time, and the ability to meet timing requirements.

This project presents a comparative study of three scheduling approaches: LIFO (Last In, First Out), RM (Rate Monotonic), and EDF (Earliest Deadline First). These approaches differ in how they assign execution order and priorities to tasks.

2. Project Objectives 

The main objectives of this research are:

To explain the basic concepts of task and process scheduling. To describe the operating principles of the LIFO scheduling approach. To introduce the RM algorithm and its fixed-priority mechanism. To explain the EDF algorithm and its dynamic-priority mechanism. To compare the advantages, disadvantages, and limitations of these approaches. To examine their behavior through examples and scheduling diagrams. To discuss their applications in operating systems and real-time systems. To identify the factors that influence the selection of an appropriate scheduling algorithm. 3. Overview of the Algorithms 3.1. LIFO (Last In, First Out) 

LIFO is a queue-processing principle in which the most recently added item is processed or removed first. It is commonly associated with stack data structures.

In a scheduling context, a LIFO-based approach prioritizes the most recently arrived task. Its behavior can be useful in particular stack-based or specialized processing scenarios, but it may cause older tasks to wait for a long time.

3.2. RM (Rate Monotonic) 

Rate Monotonic is a fixed-priority scheduling algorithm designed for periodic real-time tasks. Tasks with shorter periods receive higher priorities, while tasks with longer periods receive lower priorities.

RM is relatively predictable because task priorities remain fixed. However, its ability to schedule all tasks depends on factors such as execution times, task periods, and deadlines.

3.3. EDF (Earliest Deadline First) 

Earliest Deadline First is a dynamic-priority scheduling algorithm that prioritizes the task with the closest absolute deadline.

Unlike RM, EDF can change task priorities as deadlines approach. Under suitable assumptions, EDF can achieve high processor utilization on a single processor while meeting all task deadlines.

4. Comparison Criteria 

The algorithms are examined using the following criteria:

Priority assignment: How tasks are selected for execution. Preemption: Whether a running task can be interrupted by another task. Response time: How quickly a task begins or completes its work. Deadline satisfaction: The ability to finish tasks before their deadlines. Processor utilization: How effectively CPU time is used. Predictability: How consistently the algorithm behaves under known workloads. Implementation complexity: The effort required to implement and manage the algorithm. Starvation risk: The possibility that some tasks may wait indefinitely. 5. Advantages and Limitations 

LIFO has a simple processing principle, but older tasks may experience long delays. RM provides fixed priorities and predictable behavior, making it useful in many periodic real-time systems. EDF offers flexible priority assignment and can make efficient use of a processor under appropriate conditions, although its dynamic priorities require ongoing deadline management.

No single approach is best for every situation. The most appropriate choice depends on task characteristics, timing constraints, system architecture, and implementation requirements.

6. Real-World Applications 

Scheduling concepts are relevant to operating systems, embedded systems, industrial controllers, robotics, and other computing environments.

RM and EDF are particularly relevant to real-time scheduling, where tasks must meet timing constraints. LIFO is more directly associated with stack-based processing and specialized queueing scenarios than with conventional real-time scheduling.

7. Research Methodology 

This study uses a descriptive and comparative approach. It introduces the operating principles of each algorithm, examines their strengths and limitations, and uses scheduling examples and diagrams to illustrate differences in execution order and priority assignment.

The comparison focuses on conceptual understanding rather than claiming that one algorithm performs best in every possible workload.

8. Conclusion 

LIFO, RM, and EDF represent different approaches to processing order and scheduling priorities. LIFO follows a last-in-first-out principle, RM assigns fixed priorities according to task periods, and EDF selects tasks based on their nearest absolute deadlines.

Understanding these differences helps explain how scheduling decisions affect system behavior. The final selection should be based on the system's requirements, task model, and timing constraints.

9. Keywords 

Scheduling Algorithms, LIFO, Last In First Out, Rate Monotonic, RM, Earliest Deadline First, EDF, CPU Scheduling, Real-Time Systems, Operating Systems, Task Scheduling.

10. Author 

Student Name: Fatemeh Garmeh

Project Title: Comparison of LIFO, RM, and EDF Scheduling Algorithms

