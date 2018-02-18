import web

db_host = 'ehc1u4pmphj917qf.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'q7ac5p7jf0wsp8iz'
db_user = 'ug02a4kwu9wlhtdj'
db_pw = 'bhskxq1ob77vwe9u'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )