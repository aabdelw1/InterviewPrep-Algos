const process = async (api) => {
  let data
  try {
    data = await api('Get', '/items')
  } catch (error) {
    return false
  }

  const validEvents = ['search_changed', 'class_viewed', 'class_reserved', 'search_failed']
  const validatedEvents = {}
  const invalidIDs = []

  data.map(e => {
    if(validEvents.includes(e.name)) {
      if(!validatedEvents[e.name]){
        validatedEvents[e.name] = 0
      }
      validatedEvents[e.name] += 1
    } else {
      invalidIDs.push(e.id)
    }
  })
  try {
    const [resutl1, result2] = await Promise.all([api("POST", '/aggregates', validatedEvents), api("POST", '/junk', invalidIDs)])
  } catch (error) {
    return false
  }

}

function iterateNestedObject(obj) {
  for (let key in obj) {
    if (typeof obj[key] === 'object') {
      // Recursively call the function for nested objects
      iterateNestedObject(obj[key]);
    } else {
      // Perform desired operation or access information
      console.log(`Key: ${key}, Value: ${obj[key]}`);
    }
  }
}

