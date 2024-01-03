# Data Science UCSB W24 project-idea-reviewer

This app allows pipeline leaders to set up the club members
in the project piepline so that each one can:

1. Enter one project idea
2. Once they have entered a project idea,
   rate other club members project ideas.

Some rules that are enforced:

1. Each club member must enter a project idea before they
   can see other club members project ideas
2. Each club member should rate at least five other
   project ideas.
3. TODO: Each project idea should receive at least five ratings.

Pipeline Leader Features:

1. As a pipeline leader, I can upload a CSV file of club members
   in egrades format, and it will populate a club members
   table with
   first name, last name, email and perm number.
2. As a pipeline leader, I can do delete on
   the club members table.
3. As a pipeline leader, I can upload a CSV that will add
   a new club members without deleting anyone else
   (MVP crud substitute).
4. As a pipeline leader I can copy/paste project ideas
   and/or ratings
   into a Google Sheet.
5. TODO: The index page for project ideas shows number of
   ratings and average rating.

Club Member Features, Project Entry

1. As a club member, I can enter a project title, and a
   brief description. There is a minimum and maximum
   word length.

Club Member Features, Project Rating

1. As a club member, I can see how many additional ratings
   I have to enter.
2. TODO: As a club member/instructor, I can see how many additional ratings
   the class needs to enter to be done.
   (Admin can do it by looking project index page,
   and sorting by #ratings.)
3. As a club member, enter ratings.
   I will not be shown my own project, nor any idea
   I have already rated.
4. When rating, I am shown the project idea, and can
   choose 1 through 5, and enter a comment.
5. TODO: The comment has a minimum and maximum word length.
6. TODO: When no more ratings are needed, I can continue
   to enter extra ratings.

# Configuration for OAuth

See instructions at <https://ucsb-cs48.github.io/topics/oauth_google_setup>

After configuring OAuth:

- Use `mvn spring-boot:run` to run on localhost

To run tests: `mvn test`

Note that for Heroku, you will need to login with the `heroku login` command line tool
in order to be able to run the script that setup up Heroku credentials.
