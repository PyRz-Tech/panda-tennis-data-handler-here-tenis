## Which API Should I Pick?

Yo, there’s a ton of API types out there, each with its own deal. Let’s break ‘em down quick:

- **REST API (Representational State Transfer)**: The cool kid everyone loves. It uses HTTP stuff like GET, POST, PUT, DELETE and sends data as JSON or sometimes XML. Every request’s its own thing, so it’s chill and perfect for most projects. *We’re going with this one* ‘cause it’s dead simple, and free APIs got those pesky rate limits, so we don’t need real-time drama.
- **SOAP API (Simple Object Access Protocol)**: Bit of an old-timer. Only speaks XML, super strict, and more secure, but it’s kinda heavy and clunky to deal with.
- **GraphQL API**: The shiny new toy. You tell it exactly what data you want with one endpoint and custom queries. Neat, but way too much for our simple needs.
- **Webhook**: This one’s like, “Yo, I’ll hit you up when something happens.” Event-driven, it sends data to your app on its own. Not our vibe for this project.
- **WebSocket API**: Built for constant back-and-forth chatting. Awesome for real-time apps, but we’re keeping things low-key.
- **gRPC API**: Google’s speedy, modern setup. Crazy fast for high-performance internal systems, but not what we’re messing with here.

**Why REST API?** It’s easy-peasy, everyone uses it, and it’s perfect for snagging data without tripping over rate limits on free APIs. No need to deal with real-time nonsense.
