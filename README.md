=== some sexy name here ===
Contributors: Janukan, Jacob, Aaron
URL : http://34.71.46.196/
Project Github : https://github.com/JanukanS/GroupTasklist

=== Software Components ===
	1. MySQL Database:    # Done by Aaron
		a.Stores data on task lists
		b.able to be modified through python functions
	2. Backend Server Software:   # Done by Jacob
		a.Implemented in Python with FastAPI
		b.Defines a REST API that will call python functions to modify the database
		c.Defines a websocket connection that will tell the client page to refresh on update
	3. Frontend Server:  #Done by Janukan
		a.Implemented in python with Jinja2 and served through FastAPI (can probably be combined with backend server)
	4.Bonus Component:   #Done by Janukan
		Ability to see current tasklist with a text, implemented with Twilio

=== Description ===
A Task Management Software 
A host/user can create a private room which can be joined by other users to do tasks created by them.

=== Notes ===

--- MySQL Database and Database Manipulating Functions ---
1. Database Tables
2. Required Functions
	a. Function to clear data in the tables
	b. create a tasklist room (similar to JackBox Games), room should be referenced by a unique 4 letter code. Probably easiest to have the code be in uppercase i.e. EYTR
	c. create a task in the tasklist, the task should be stored along with the name of the task’s author and the time create
	d. state a task is started with the name of the person doing the task and the time started
	e. State a task is completed, reuse the name of the person who did the task and record the time completed. The task should not be deleted in the database
	f. Retrieve all tasks(unfinished, in progress or complete) from a specific tasklist room

--- Backend Server API ---
1.GET task_table
	a. Input: string 4-letter room key i.e. EWTY
	b. Output: Json response of a dictionary with 7 key-value pairs
		Task names [String]: names of the tasks
		Task Creator[String]: names of person who created task
		Creation Time [DateTime?]: time the task was created
		In Progress Name [String]: Name of person currently doing project, if there isn’t anybody currently working on the task. Its respective array entry would be blank
		In Progress Time [DateTime?]: Time the task was started, respective entry would be empty if the task was not started
		Completion Person [ String]: Name of person who completed the task, respective entry is empty if task is not complete
		Completion Time: [DateTime?]: Time that task was completed, empty for respective task if it is complete
		Not sure what format datetime should be in, probably most convenient if its in a string.
2.POST create_taskroom
	a.Input: Takes one string: taskroom creator [STRING]
	b.Output: 4 letter room key
	c.Operation: 
		Should call database-interface function to create a room
		Return the new room key (4 letter combination)
3.POST create_task
	a.Input: Takes two strings: task title and task author
	b.Output: success/failure state (true/false)
4.POST start_task:
	a.Input: Task Identifier, person, roomno
	b.Output: success/failure state
5.POST finish_task:
	a.Input: Task Identifier, Person, roomno
	b.Output: success/failture state

--- Frontend Pages ---
1.Homepage: generate taskrooms from here
	a.Has a form that accepts a username, completing it will lead to the taskroom page
2.Room Entry Page: this link will be shared, allows people to join the taskroom
 a.Has a form that accepts username, completing it will lead to the taskroom page
3.Taskroom: Contains the actual tasklist, link should be unique to each person
	a.Display room entry page link to be copied
	b.Displays table of tasks
		Task table data should be obtained from a get request
		Task row should have: task name, created by & creation time, progress started by & progress start time, completion with person & time
		If a task is not in progress, there should be button/link to send a post REST request. This request will let the task change to in - progress
		If a task is in progress, there will be a button/link to sent a post request to complete the task
		Bottom row should have an input textbox to create a new task, submit button will send a post request to create a task
4.Websocket connection: 
	a.subscribed to room code, 
	b.websocket used for the server to send an update signal. 
	c.Upon receiving the update signal, page should rebuild the task table through calling the get request a second time
