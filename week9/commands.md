# Find all the documents in the collection restaurants
``db.restaurants.find()``
# Find the fields restaurant_id, name, borough and cuisine for all the documents in the collection restaurant.
``db.restaurants.find({}, {restaurant_id: true, name: true, borough: true, cuisine:true})``
# Find the first 5 restaurant which is in the borough Bronx.
``db.restaurants.find({borough: "Bronx"}).sort({restaraunt_id: 1}).limit(5)``
# Find the restaurant Id, name, borough and cuisine for those restaurants which prepared dish except 'American' and 'Chinees' or restaurant's name begins with
letter 'Wil’.
``db.restaurants.find({$or: [{cuisine: {$nin: ["American", "Chinese"]}}, {name: /^Wil/}]}, {restaurant_id: true, name: true, borough: true, cuisine:true})``
# Find the restaurant name, borough, longitude and attitude and cuisine for those restaurants which contains 'mon' as three letters somewhere in its name.
``db.restaurants.find({name: /.*mon.*/i}, {coord: true, name: true, borough: true, cuisine:true})``

# Find the restaurant Id, name, borough and cuisine for those restaurants which belong to the borough Staten Island or Queens or Bronx or Brooklyn.
``db.restaurants.find({borough: {$in: ["Staten Island", "Queens", "Brooklyn"]}}, {restaurant_id: true, name: true, borough: true, cuisine:true})``
