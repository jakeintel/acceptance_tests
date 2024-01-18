## Possible Tests Happy Path Tests ##
# ~ 10


## Is there a 20x response at the account level?


## As a Device ##

# POST: api/v2/devices/:id/manifests
#   -> 202 & pm.expect(jsonData.processed_message.msg[0].validated).to.eql(true)
#   Can go deeper with different manifests; the return body contains a list of results

# POST: /api/v2/partitions/:partitions/manifests -> 403

# GET: api/v2/accounts/:account/vulnerabilities -> 403

# GET: api/v2/partitions/:partition/vulnerabilities -> 403

# GET: api/v2/devices/:device/vulnerabilities -_ TBD

# GET: /api/v2/accounts/:account/processed -> 403

# GET: api/v2/partitions/:partition/processed -> 403

# ?? Should there be a processed for a device?


## As an ISV ##

# POST: api/v2/devices/:id/manifests
# -> 403

# POST: /api/v2/partitions/:partitions/manifests 
#   -> 202 & pm.expect(jsonData.processed_message.msg[0].validated).to.eql(true)
#   Can go deeper with different manifests; the return body contains a list of results

# GET: api/v2/accounts/:account/vulnerabilities -> 403

# GET: api/v2/partitions/:partition/vulnerabilities -> 200
#   -> pm.expect(jsonData.detail.result.data_count).to.be.above(0)

# GET: api/v2/devices/:device/vulnerabilities -> 200
#   -> pm.expect(jsonData.detail.result.data_count).to.be.above(0)

# GET: /api/v2/accounts/:account/processed -> 403

# GET: api/v2/partitions/:partition/processed -> 200
#   -> pm.expect(jsonData.detail.result.data_count).to.be.above(0);

# In the workflow, what do we execute against? If anything

# How do we control which env test run against?