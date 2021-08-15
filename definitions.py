import mysql.connector

from dao import user_task_classes
from dao.user_task_classes import ForUser


def ConnectToDB():
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Telecomee*23',
        database='python'
    )
    return db


def CreateUser():
    mydb = ConnectToDB()
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE user (user_id INT, user_name VARCHAR(20),phone VARCHAR(20), role VARCHAR(20), dob VARCHAR(20), created_on  VARCHAR(20), modified_on VARCHAR(20))")
    mydb.commit()


def InsertIntoUser(user_task_classes):
    mydb = ConnectToDB()
    mycursor = mydb.cursor()
    sql = "INSERT INTO user (user_id, user_name, phone, role, dob, created_on, modified_on) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (user_task_classes.user_id, user_task_classes.user_name, user_task_classes.phone, user_task_classes.role, user_task_classes.dob,
               user_task_classes.created_on, user_task_classes.modified_on)
    mycursor.execute(sql, val)
    mydb.commit()


"""
user1 = ForUser(20266, "Joey", "7780572743", "TTS", "29-03-2000", "12-08-2021", "13-08-2021")
InsertIntoUser(user1)"""


def CreateTask():   # creating task
    mydb = ConnectToDB()
    mycursor = mydb.cursor()
    mycursor.execute(
        'CREATE TABLE task (task_id INT, name VARCHAR(20), description VARCHAR(255), status VARCHAR(20), priority INT, '
        'notes VARCHAR(255), bookmark VARCHAR(20), owner_id INT, creator_id INT, created_on VARCHAR(20), '
        'modified_on VARCHAR(20))')
    mydb.commit()


def InsertIntoTask(user_task_classes):
    mydb = ConnectToDB()
    mycursor = mydb.cursor()
    sql = "INSERT INTO task (task_id, name, description, status, priority, notes, bookmark, owner_id, creator_id, created_on, modified_on) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (user_task_classes.task_id, user_task_classes.name, user_task_classes.description, user_task_classes.status,
           user_task_classes.priority, user_task_classes.notes, user_task_classes.bookmark, user_task_classes.owner_id,
           user_task_classes.creator_id, user_task_classes.created_on, user_task_classes.modified_on)
    mycursor.execute(sql, val)
    mydb.commit()


"""
task1 = (101, "Goal Identification", "Discussion with team about the goal", "Ongoing", 1, "Allocating tasks to be done", "yes",20260,12,"12-08-2021","13-08-2021")
InsertIntoTask(task1)"""


def UpdatePriority(task_id, priority):
    db = ConnectToDB()
    cursor = db.cursor()
    sql = "UPDATE task SET priority=%s WHERE task_id =%s"
    val = (priority, task_id)
    cursor.execute(sql, val)
    db.commit()


def UpdateNotes(task_id, notes):
    db = ConnectToDB()
    cursor = db.cursor()
    sql = "UPDATE task SET notes=%s WHERE task_id =%s"
    val = (notes, task_id)
    cursor.execute(sql, val)
    db.commit()


def UpdateBookmark(task_id, bookmark):
    db = ConnectToDB()
    cursor = db.cursor()
    sql = "UPDATE task SET bookmark=%s WHERE task_id =%s"
    val = (bookmark, task_id)
    cursor.execute(sql, val)
    db.commit()


def UpdateStatus(task_id, status):
    db = ConnectToDB()
    cursor = db.cursor()
    sql = "UPDATE task SET status=%s WHERE task_id =%s"
    val = (status, task_id)
    cursor.execute(sql, val)
    db.commit()

# method to get all tasks  for a given user


def AllTasksUser():
    db = ConnectToDB()
    cursor = db.cursor()
    sql = "SELECT user.user_name as user, task.name as task_name FROM user INNER JOIN task ON user.user_id = task. owner_id"
    cursor.execute(sql)
    result = cursor.fetchall()
    for x in result:
        print(x)


# get all  tasks based on the status
def TasksBasedOnStatus(status):
    db = ConnectToDB()
    cursor = db.cursor()
    sql = "SELECT name FROM task WHERE status =%s"
    val = (status, )
    cursor.execute(sql, val)
    result = cursor.fetchall()
    for x in result:
        print(x)


# get all tasks (without any condition)
def AllTasks():
    db = ConnectToDB()
    cursor = db.cursor()
    sql = 'SELECT name FROM task'
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)

"""
db = ConnectToDB()
cursor = db.cursor()
sql = "UPDATE user SET role = 'Developer' WHERE userid=20264"
cursor.execute(sql)
db.commit()"""