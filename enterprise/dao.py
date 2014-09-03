from pymongo import MongoClient, DESCENDING
from datetime import datetime
client = MongoClient()
db = client.greenbuilding


def create_log(log):
    log_id = db.logs.insert(log)


def find_logs(project_id):
    print 'project id:{}'.format(project_id)
    result = db.logs.find({'project_id': int(project_id)}).sort('time', DESCENDING)
    #Note that you can only iterate over cursor only once! Please do not iterate the cursor here!
    return result


event = {
    'time':  datetime.now(),
    'project_id': 7,
    'message': 'test'
}
#create_log(event)
print db.logs.find().count()
logs = find_logs(8)
for log in logs:
    print log
