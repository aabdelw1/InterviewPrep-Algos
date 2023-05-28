const aggregator = new EventAggregator();

function callback1(data) {
  console.log('Callback 1:', data);
}

function callback2(data) {
  console.log('Callback 2:', data);
}

aggregator.subscribe('event1', callback1);
aggregator.subscribe('event1', callback2);

aggregator.publish('event1', 'Hello, World!');
// Output:
// Callback 1: Hello, World!
// Callback 2: Hello, World!

aggregator.unsubscribe('event1', callback1);

aggregator.publish('event1', 'Goodbye!');
// Output:
// Callback 2: Goodbye!

class EventAggregator {
  constructor() {
    this.subscriptions = {};
  }

  subscribe(event, callback) {
    if (!this.subscriptions[event]) {
      this.subscriptions[event] = [];
    }

    this.subscriptions[event].push(callback);
  }

  unsubscribe(event, callback) {
    if (this.subscriptions[event]) {
      this.subscriptions[event] = this.subscriptions[event].filter(
        cb => cb !== callback
      );
    }
  }

  async publish(event, data) {
    const callbacks = this.subscriptions[event];
    if (callbacks) {
      // Iterate through the callbacks and execute them asynchronously
      for (const callback of callbacks) {
        await callback(data);
      }
    }
  }
}