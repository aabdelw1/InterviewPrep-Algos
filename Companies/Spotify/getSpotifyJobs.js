const fs = require('fs');

let curJobs = []
fs.readFile('/Users/Ammar/Desktop/Playground/Spotify/output.txt', 'utf8', (err, data) => {
  if (err) throw err;
  curJobs = data.split('\n');
});


async function getSpotifyJobData() {
  try {
    const response = await fetch("https://api-dot-new-spotifyjobs-com.nw.r.appspot.com/wp-json/animal/v1/job/search?l=remote-americas%2Cremote-estamericas-remote%2Cnew-york&c=backend%2Cclient-c%2Cdata%2Cmachine-learning%2Cmobile%2Ctech-research%2Cweb", {
      "headers": {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "sec-ch-ua": "\"Chromium\";v=\"112\", \"Google Chrome\";v=\"112\", \"Not:A-Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "cross-site",
        "Referer": "https://www.lifeatspotify.com/",
        "Referrer-Policy": "strict-origin-when-cross-origin"
      },
      "body": null,
      "method": "GET"
    });

    if (response.ok) {
      const jsonData = await response.json();
      return jsonData;
    } else {
      throw new Error('Network response was not ok.');
    }
  } catch (error) {
    console.error('Error fetching Spotify job data:', error);
  }
}

const writetoFile = (arr) => {
  const output = arr.map(job => job).join('\n');
  fs.writeFile('/Users/Ammar/Desktop/Playground/Spotify/output.txt', output, (err) => {
    if (err) throw err;
    console.log('All Jobs:\n');
    printToConsole(arr)
  });
}

const printToConsole = (arr) => {
  arr.forEach(el => console.log('-', el))
  console.log('\n')
}

async function printSpotifyJobData() {
  let newJobs = []
  try {
    const jsonData = await getSpotifyJobData();
    jsonData.result.forEach(element => {
      newJobs.push(element.text)
    });
    if(JSON.stringify(curJobs)==JSON.stringify(newJobs)){
      console.log("No jobs removed or added\n")
      printToConsole(newJobs)

    } else{
      if(curJobs.length > newJobs.length){
        console.log("Job postings taken down:\n")
        const diff = curJobs.filter(item => !newJobs.includes(item))
        printToConsole(diff)
        writetoFile(newJobs)

      } else if (newJobs.length > curJobs.length){
        console.log("New job postings:\n")
        const diff = newJobs.filter(item => !curJobs.includes(item))
        const diff1 = curJobs.concat(diff)
        printToConsole(diff)
        writetoFile(diff1)
      }
    }
  } catch (error) {
    console.error(error);
  }
}



printSpotifyJobData();
