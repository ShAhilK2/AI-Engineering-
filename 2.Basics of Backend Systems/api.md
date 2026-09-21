API
Application Programming Interface

API is a communication bridge between different software applications.

API stands for Application Programming Interface. It is a mechanism that allows different software applications or systems to communicate with each other. For example, in a MERN application, the React frontend communicates with the Node.js and Express backend through APIs to send requests and receive data.”

“For example, GET /api/users can retrieve users, POST /api/users can create a new user, PATCH /api/users/:id can update specific user fields, and DELETE /api/users/:id can delete a user.”

Framework vs library

“The main difference between a library and a framework is who controls the flow of the application. With a library, we call the library when we need it. With a framework, the framework controls the application flow and calls our code when needed.”

Library → React

My Code
↓
I call React
↓
React does the work

Framework → Next.js / NestJS

Framework
↓
Controls application flow
↓
Calls my code when needed

“Is React a framework or library?”

You can answer:

“React is a JavaScript library for building user interfaces. We use React APIs and components when we need them, while React itself doesn't enforce the complete structure of the application.”

“REST stands for Representational State Transfer. It is an architectural style for designing web APIs. REST APIs use HTTP methods such as GET, POST, PUT, PATCH, and DELETE to perform operations on resources, and they are generally stateless, meaning each request contains the information needed to process it.”

If the interviewer asks “What are the principles of REST?”, mention:

Client–Server architecture
Stateless
Cacheable
Uniform Interface
Layered System
Code-on-Demand (optional)

alternatives of Rest

Main alternatives
Technology Best suited for Key idea
GraphQL Flexible data fetching Client asks for exactly the data it needs
gRPC High-performance service-to-service communication Uses Protocol Buffers and HTTP/2
SOAP Enterprise/legacy systems Strict XML-based protocol
WebSockets Real-time communication Persistent two-way connection
Webhooks Event notifications Server sends data when an event occurs

🧠 Interview-friendly explanation

REST

Client → HTTP Request → Server → Response

GraphQL

Client → Query exactly what it needs → Server → Response

gRPC

Service A ⇄ Service B
(high-performance communication)

WebSocket

Client ⇄ Persistent connection ⇄ Server
⭐ For a MERN developer

I'd remember these four first:

REST → GraphQL → gRPC → WebSockets

And don't say they are simply "better alternatives." Each solves different problems.

Guidelines of REST API Design

Rest prefers a client server communication should happen over http
Rest prefers JSON as the format to send and receive data

Rest gives guidelines on how urls should look like :

in rest, the main source of info is considered as a Resource
Ex Tweet => Resource
create tweet => Action
delete tweet => Action
update tweet => Action
get tweet => Action
user => Resource
create user => Action
delete user => Action
update user => Action
get user => Action

the endpoints /url should use Nouns and not verbs
For example :
/users instead of /getUsers
Nouns shoud/expected be plural
for example : /users, /tweets, /posts

Every Rest endpoints should be depend along with a HTTP method
for example :
GET /users -> get/retrieve all users
POST /users -> create a user
PUT /users -> update a user
PATCH /users -> partial update
DELETE /users -> delete a user

/blogs => get all blogs
/blogs/:id => get a specific blog

/blogs => POST => create a blog
/blogs/:id => PUT => update a blog
/blogs/:id => DELETE => delete a blog

Information send in request body should be in JSON format
Properties in update is in request body

For relationship , we use nesting
/blogs/13/comments => get all comments for blog 13
/blogs/13/comments/45 => get comment 45 for blog 13

/blogs/13/comments => POST => create a comment for blog 13
/blogs/13/comments/45 => PUT => update comment 45 for blog 13
/blogs/13/comments/45 => DELETE => delete comment 45 for blog 13

Dont use more than 3 levels of nesting
for example => /blogs/13/comments/45/replies/67

Versioning => /api/v1/users
means version 1 of the api
what use for ?

- when we make changes to the api, we can version it
- for example, if we make a breaking change to the api, we can version it
- for example, if we make a non-breaking change to the api, we can version it

Newer app uses versioning to support different client versions
Older Version app uses versioning to support different client versions

backward compatibility means that the api should be able to support different client versions

Sending data can be done in 3 ways :

1.  Query Parameters
    Example : /users?name=John&age=25
2.  Request Body
    Example : /users (with JSON body)
3.  Path Parameters
    Example : /users/123

Framework based on rest convention are :

- Express.js
- FastAPI
- Django REST Framework
- Spring Boot
- etc.

CRUD Operations :

- Create (POST)
- Read (GET)
- Update (PUT/PATCH)
- Delete (DELETE)

REST SUPPORT CRUD Operations MEANS that the api should support these operations

REST Constraints:

- Client Server
- Stateless
- Cacheable
- Uniform Interface
- Layered System
- Code on Demand (optional)
