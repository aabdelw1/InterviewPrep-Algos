const handleClick = async event => {
  console.log('before');

  await delay(1000);

  console.log('after');
};

async function init() {
  console.log(1);
  await sleep(1000);
  console.log(2);
}

function sleep(ms) {
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

init()