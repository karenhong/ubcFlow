-- Some data to populate the database with
INSERT INTO Course VALUES ('CPSC 110','Computation, Programs, and Programming','Fundamental program and computation structures. Introductory programming skills. Computation as a tool for information processing, simulation and modeling, and interacting with the world.', 1);
INSERT INTO Course VALUES ('CPSC 221','Basic Algorithms and Data Structures','Design and analysis of basic algorithms and data structures; algorithm analysis methods, searching and sorting algorithms, basic data structures, graphs and concurrency.', 2);
INSERT INTO Course VALUES ('CPSC 213','Introduction to Computer Systems','Software architecture, operating systems, and I/O architectures. Relationships between application software, operating systems, and computing hardware; critical sections, deadlock avoidance, and performance; principles and operation of disks and networks.', 2);
INSERT INTO Course VALUES ('CPSC 304','Introduction to Relational Databases','Overview of database systems, ER models, logical database design and normalization, formal relational query languages, SQL and other commercial languages,data warehouses, special topics.', 3);
INSERT INTO Course VALUES ('CPSC 314','Computer Graphics','Human vision and colour; geometric transformations; algorithms for 2-D and 3-D graphics; hardware and system architectures; shading and lighting; animation.', 3);
INSERT INTO Course VALUES ('CPSC 410','Advanced Software Engineering','Specification, design, construction and validation of multi-version software systems.', 4);
INSERT INTO Course VALUES ('CPSC 445','Algorithms in Bioinformatics','Sequence alignment, phylogenetic tree reconstruction, prediction of RNA and protein structure, gene finding and sequence annotation, gene expression, and biomolecular computing.', 4);

INSERT INTO User VALUES ('k@gmail.com', 'Kara', 'Song', 'password123');
INSERT INTO User VALUES ('john@yahoo.com', 'John', 'Doe', 'password123');
INSERT INTO User VALUES ('anna@gmail.com', 'Anna', 'May', 'password123');
INSERT INTO User VALUES ('jay@hotmail.com', 'Jay', 'Lee', 'password123');

INSERT INTO Review VALUES ( 1, 4, 'Great Course!', 'Learned a lot from this course! Would recommend', 'anna@gmail.com', 'CPSC 410');
INSERT INTO Review VALUES ( 2, 1, 'Do not take this course!', 'Terrible course! Not well organized at all!', 'john@yahoo.com', 'CPSC 445');
INSERT INTO Review VALUES ( 3, 3, 'Ehh', 'This course was alright. Nothing too special about it.', 'jay@hotmail.com', 'CPSC 221');
INSERT INTO Review VALUES ( 4, 5, 'Amazing!', 'Everybody needs to take this course!', 'k@gmail.com', 'CPSC 213');
INSERT INTO Review VALUES ( 5, 5, 'Would recommend', 'This was a great course!', 'k@gmail.com', 'CPSC 304');
INSERT INTO Review VALUES ( 6, 3, 'OK I guess', 'Learned some things...probably', 'jay@hotmail.com', 'CPSC 304');
INSERT INTO Review VALUES ( 7, 2, 'Stay away', 'Do not take this course!', 'anna@gmail.com', 'CPSC 304');
