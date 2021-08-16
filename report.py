# method to get all tasks  for a given user
from dao.definitions import ConnectToDB

# method to get all tasks  for a given user


def AllTasksUser(userid):
    db = ConnectToDB()
    cursor = db.cursor()
    sql = "SELECT user.user_name as user, task.name as task_name FROM user INNER JOIN task ON user.user_id = task. owner_id WHERE user_id = %s"
    val = (userid, )
    cursor.execute(sql, val)
    result = cursor.fetchall()
    for x in result:
        return result


# get all  tasks based on the status
def TasksBasedOnStatus(status):
    db = ConnectToDB()
    cursor = db.cursor()
    sql = "SELECT name FROM task WHERE status =%s"
    val = (status, )
    cursor.execute(sql, val)
    result = cursor.fetchall()
    for x in result:
        return result


# get all tasks (without any condition)
def AllTasks():
    db = ConnectToDB()
    cursor = db.cursor()
    sql = 'SELECT name FROM task'
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def AllTasksUser(userid):
    db = ConnectToDB()
    cursor = db.cursor()
    sql = "SELECT user.user_name as user, task.name as task_name FROM user INNER JOIN task ON user.user_id = task. owner_id WHERE user_id = %s"
    val = (userid, )
    cursor.execute(sql, val)
    result = cursor.fetchall()
    for x in result:
        return result


# get all  tasks based on the status
def TasksBasedOnStatus(status):
    db = ConnectToDB()
    cursor = db.cursor()
    sql = "SELECT name FROM task WHERE status =%s"
    val = (status, )
    cursor.execute(sql, val)
    result = cursor.fetchall()
    for x in result:
        return result


# get all tasks (without any condition)
def AllTasks():
    db = ConnectToDB()
    cursor = db.cursor()
    sql = 'SELECT name FROM task'
    cursor.execute(sql)
    result = cursor.fetchall()
    return result
