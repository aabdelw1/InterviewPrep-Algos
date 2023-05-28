function createEventAggregator() {
  const subscriptions = {};

  function subscribe(event, callback) {
    if (!subscriptions[event]) {
      subscriptions[event] = [];
    }

    subscriptions[event].push(callback);
  }

  function unsubscribe(event, callback) {
    if (subscriptions[event]) {
      subscriptions[event] = subscriptions[event].filter(
        cb => cb !== callback
      );
    }
  }

  async function publish(event, data) {
    const callbacks = subscriptions[event];
    if (callbacks) {
      // Iterate through the callbacks and execute them asynchronously
      for (const callback of callbacks) {
        await callback(data);
      }
    }
  }

  return {
    subscribe,
    unsubscribe,
    publish
  };
}

const eventAggregator = createEventAggregator();

function callback1(data) {
  console.log('Callback 1:', data);
}

function callback2(data) {
  console.log('Callback 2:', data);
}

eventAggregator.subscribe('event1', callback1);
eventAggregator.subscribe('event1', callback2);

eventAggregator.publish('event1', 'Hello, World!');
// Output:
// Callback 1: Hello, World!
// Callback 2: Hello, World!

eventAggregator.unsubscribe('event1', callback1);

eventAggregator.publish('event1', 'Goodbye!');
// Output:
// Callback 2: Goodbye!