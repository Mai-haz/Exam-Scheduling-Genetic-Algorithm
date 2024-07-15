
# Exam Scheduling Genetic Algorithm

This project implements a genetic algorithm to optimize the scheduling of exams based on given constraints such as student availability, teacher availability, and room availability.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Algorithm Overview](#algorithm-overview)
- [Classes and Structure](#classes-and-structure)
- [Sample Output](#sample-output)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The project aims to automate the process of scheduling exams in educational institutions using a genetic algorithm approach. It takes into account various constraints like:

- Student course schedules
- Teacher availability
- Room availability
- Avoidance of exam time conflicts for students
- Optimization of exam schedules based on predefined fitness criteria

## Features

- **Random Initialization**: Initial schedules are randomly generated based on input data.
- **Genetic Algorithm**: Implements genetic operations such as crossover and mutation to evolve better schedules over generations.
- **Fitness Calculation**: Evaluates each schedule based on conflicts and constraints to determine its fitness.
- **Pretty Output**: Utilizes `prettytable` to display schedules in a readable format.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
   
2. Install the required dependencies:
   ```bash
   pip install prettytable numpy pandas
   ```
   
3. Run the main script:
   ```bash
   python exam_scheduling.py
   ```

## Usage

Once installed, you can modify the input data in `exam_scheduling.py` to suit your specific requirements. Adjust parameters such as the number of students, courses, teachers, rooms, and exam times as needed.

## Algorithm Overview

The algorithm follows these steps:

1. **Initialization**: Randomly assigns exams to days and time slots based on input data.
2. **Fitness Calculation**: Evaluates each schedule's fitness by checking for conflicts (e.g., same student having exams at the same time).
3. **Genetic Operations**: Uses crossover and mutation to create new generations of schedules.
4. **Selection**: Selects schedules with higher fitness to create the next generation.
5. **Termination**: Stops when a schedule with perfect fitness (no conflicts) is found or after a specified number of generations.

## Classes and Structure

- **InputData**: Manages input data such as student schedules, teacher availability, and room availability.
- **Schedule**: Represents a schedule with exams, manages fitness calculation and sorting of exams.
- **Population**: Represents a population of schedules.
- **GeneticAlgorithm**: Implements genetic operations like crossover and mutation.
- **Student, Exam, Course Classes**: Represent entities with their attributes and methods for scheduling.

## Sample Output

A sample output might look like this:

```
Chromosome 1 Fitness: 0.92 Conflicting: 4
+----------+---------------+-----------+------------+---------+
| Teacher  |    Course     |   Day     |    Time    |  Room   |
+----------+---------------+-----------+------------+---------+
|   Sara   |     Maths     |  Monday   |  9:00-11:00|   C401  |
|   Ali    |     Biology   |  Monday   | 12:00-2:00 |   A301  |
...
```

## Contributing

Contributions are welcome! Fork the repository and submit a pull request with your enhancements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

