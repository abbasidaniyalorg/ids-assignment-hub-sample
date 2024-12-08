# IDS Assignment Hub Sample

This repository serves as a master framework for managing assignments in the IDS Assignment Hub. It provides tools to create, release, grade, and distribute solutions for assignments using the **nbgrader** tool.

## Github Classroom
- Assignment 1:  [GitHub Classroom Assignment Link](https://classroom.github.com/a/prXAd2nY)

### Key Features:
- **Assignment Management**: Centralized handling of assignments using nbgrader.
- **Student Repositories**: Distributes assignments to students as template repositories on GitHub Classroom.
- **Grading System**: Supports both autograded and manually graded components.
- **Secure Solutions**: This repository remains private to protect solutions and test cases, while student repositories are public.

### Note: For now, we will only use nbgrader to create assignments and release the student versions. Auto-grading will be implemented as a CI pipeline in github classroom and grades will be published and managed there. We are not using any other features of nbgrader like student submissions, feedback, manual grading etc for now.

## Workflow for Assignments

1. **Create Assignments**:
   - Write assignment questions and solutions in the `source` directory along with other required files if any.
   - Include public and hidden test cases for grading.
   - Add autograded cells as needed.

2. **Generate Student Notebooks**:  
   - Run `nbgrader generate_assignment` to create student-friendly notebooks in the `release` directory.  
   - Push these notebooks to a new GitHub repository as a **template repository** for distribution.  
   - Release the student notebooks via GitHub Classroom by using the template repository, which includes all necessary files such as data, notebooks, and other resources.

3. **Student Submission**:  
   - Students clone the template repository to complete the assignments.  
   - Public test cases provide immediate feedback during the solving process.  
   - Instructors receive student submissions via GitHub Classroom.

4. **Grading**:
   - Use the autograder to evaluate submissions, including hidden test cases which runs as a github action workflow.

5. **Release Grades and Solutions**:
   - Share grades and comments with students via feedback notebooks.

---

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone git@github.com:abbasidaniyal/ids-assignment-hub-sample.git
   cd ids-assignment-hub-sample
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize nbgrader (First Time Only)**:
   ```bash
   nbgrader quickstart ids-assignment-hub-sample
   ```

5. **Create Assignments**:
   - **Option 1: Using Jupyter Notebook UI**:
     1. Start the Jupyter server:
        ```bash
        jupyter notebook
        ```
     2. Navigate to the **Form Grader** UI.
     3. Create a new assignment.

   - **Option 2: Using Command Line**:
     1. Create an assignment directory and register it:
        ```bash
        mkdir source/"Assignment 1"
        nbgrader db assignment add --assignment="Assignment 1"
        ```
     2. Create the assignment notebook:
        ```bash
        touch source/"Assignment 1"/Assignment1.ipynb
        ```
     > Note: Consider using shell scripts to automate this process.

6. **Add Content**:
   - Write questions, solutions, and test cases in the notebook.
   - Include grading criteria and any additional files.

7. **Release Assignments**:
   ```bash
   nbgrader generate_assignment --assignment="Assignment 1"
   ```
   The student version will be available in the `release` directory. Push it to a new repository in your GitHub organization.

8. **Collect Submissions**:
   - Submissions are stored in the `submitted/<student_id>/<assignment_name>` directory.

9. **Grade Submissions**:
    - **Autograding**:
      ```bash
      nbgrader autograde "Assignment 1"
      ```
    - **Manual Grading**:
      ```bash
      nbgrader formgrade "Assignment 1"
      ```

10. **Release Feedback**:
    ```bash
    nbgrader release_feedback "Assignment 1"
    ```
    Feedback notebooks are stored in the `feedback` directory for distribution.

11. **Generate Solutions**:
    ```bash
    nbgrader generate_solution "Assignment 1"
    ```
    Solution notebooks are stored in the `release` directory for sharing post-deadline.

---

## References

- [nbgrader Documentation](https://nbgrader.readthedocs.io/en/stable/)
- [Getting Started with nbgrader](https://youtu.be/5WUm0QuJdFw)
