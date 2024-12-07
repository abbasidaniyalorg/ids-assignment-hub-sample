# ids-assignment-hub-sample

This is a sample repository for the IDS assignment hub. It acts as the master repository for the assignments. This can be viewed as a framework to create, release, grade and release solution to assignments for the students.

This uses the nbgrader tool to manage the assignments. The assignments are stored in the `source` directory. The assignments are distributed to the students using the `release` directory.

Student version of the notebooks are released as separate repositories and push to github as "template repositories".

Note: This repository will not be public as it contains all the solutions as well as the sample test cases. The student repositories will be public.

## Flow of the assignments


1. Create the assignments notebook in the `source` directory. This contains the questions and the solutions. Further, we also add the tests to the notebook. We can also have autograded answer cells in the notebook as well as manually graded cells.

2. Run the `nbgrader assign` command to create the student version of the notebooks. This will create the student version of the notebooks in the `release` directory. This will be pushed to a new repository (public) in the github organization. On github classroom, we use this repository as the template repository.

3. The students will clone the repository and work on the assignments. They will push the changes to their repository. Students will be able to use public test-cases to check their solutions and get immediate feedback. 

4. Further, after submmissioin, the instructors can run the autograder to get the final score whiich wiil also execute the hidden test-cases. If any manual grading is required, the instructors can do that as well. We can also add instructor comments to the notebooks so that students can get an insidght on the solutions. 




## Setup

1. Clone the repository

```bash
git clone git@github.com:abbasidaniyal/ids-assignment-hub-sample.git
```

2. Create a virtual environment

```bash
python3 -m venv env
source env/bin/activate
```

3. Install the requirements

```bash
pip install -r requirements.txt
```

4. Initialize the nbgrader (only needed first time)

```bash
nbgrader quickstart ids-assignment-hub-sample
```


5. Create the assignment. It is easy to do from the UI

- a. Start the notebook server
```bash
jupyter notebook
```

- b. Go to form grader in the UI of the notebook and go to formgrader
- c. Create a new assignment using the UI

OR 

In order to use the command line, we can use the following commands:


- a. Create the assignment directory and add to the database

```bash
mkdir source/Assignment\ 1
nbgrader db assignment add --assignment='Assignment 1'
```

- b. Create the jupyternotebook for the assignment
```bash
touch source/Assignment\ 1/Assignment1.ipynb
```
Note: We can create shell scripts to automate the process of creating the assignments.


6. Add the questions and solutions to the notebook. Add the tests as well along with scoring criteria.
Add any other required files in the assignment directory.

7. Release the assignment

```bash
nbgrader generate_assignment --assignment='Assignment 1'
```

This will create the student version of the notebook in the `release` directory. 

To create a new repository in the github organization, we can use the following command:

```bash
```


8. Collect student responses and store them in the `submitted` directory. Store them in the `submitted` directory in the format `submitted/<student_id>/<assignment_name>`.

Note: inorder to add student, we can use the following command:
```bash
nbgrader db student add --last-name='Doe' --first-name='John' --id='jdoe'
```
or use the UI to add the students.

9. Grade the assignment

```bash
nbgrader autograde assignment1
```

This will grade the assignment and store the grades in the `autograded` directory.

10. If needed, do manual grading using nbgrader formgrade

```bash
nbgrader formgrade assignment1
```

11. Release the grades

```bash
nbgrader release_feedback assignment1
```

This will create the feedback version of the notebook in the `feedback` directory. This can be shared with the students.


12. To create a solution version of the notebook, run the following command:

```bash
nbgrader generate_solution assignment1
```

This will create the solution version of the notebook in the `release` directory. This can be shared with the students after the deadline.


## References

- https://nbgrader.readthedocs.io/en/stable/
- https://youtu.be/5WUm0QuJdFw


