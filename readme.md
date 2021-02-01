#make mongo user
db.createUser({user: "admin",pwd: "admin",roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]})
db.createUser({user:'test',pwd:'test1234',roles:['dbOwner']})
db.createUser({user: "testUser", pwd: "testPassword", roles: [ {role: "readWrite", db: 'testDB'} ]})

 db.auth("testUser", "testPassword")