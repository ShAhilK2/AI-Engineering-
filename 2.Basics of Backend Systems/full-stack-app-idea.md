Design : A Social Media App

Browser Client

1.Computing Capabilties => How easily we can execute the instruction
2.Storage Capabilities => How easily we can store the da

Storage Option
1.Secondary Storage -> HDD/SSD ROM (Persistent)
2.Primary Storage -> RAM
3.Cache - > L1,L2,L3

Caching the data means storing data on a relational faster storage

Back of the envelope calculation
Capacity Estimations

Latency
Total time/delay happening since the start of a request till the time ,receives the response

Factors contributing to latency

1. External latency → Delay caused by things outside your application/system.

Examples:

Network/internet delay(Cross Continent Call)
A Global Network Latency

DNS lookup

API calls to third-party services

Database hosted on another server

Cloud service response time

Physical distance between servers

2. Internal latency → Delay caused by things inside your application/system.

Examples:

Slow code execution

CPU processing

Memory access

Database queries within your system

Locks/contention between processes

Disk I/O

Queues and internal services

https://redis.io/glossary/cache-memory/

thrashing in os

Scaling =>
Horizontal Scaling
Vertical Scaling

Scaling is the process of adding computing resources to handle increased workload, achieved through two primary methods: Horizontal Scaling and Vertical Scaling.

Vertical Scaling (Scale Up) involves increasing the power of a single existing machine by adding more CPU, RAM, or storage. It is simpler to implement and suits monolithic or stateful applications but is limited by hardware ceilings and creates a single point of failure.
Horizontal Scaling (Scale Out) involves adding more identical machines or nodes to a resource pool to distribute the load. It offers near-limitless scalability, better fault tolerance, and handles unpredictable traffic well, but requires complex load balancing and distributed system architecture.

Stateful System vs Stateless System
s
