from pymongo import MongoClient
from datetime import datetime
client = MongoClient()
db = client.greenbuilding


def create_log(log):
    log_id = db.logs.insert(log)


def find_logs(project_id):
    print 'project id:{}'.format(project_id)
    result = db.logs.find({'project_id': int(project_id)})
    #Note that you can only iterate over cursor only once!
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
