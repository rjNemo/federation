import {ApolloServer} from "apollo-server";
import {ApolloGateway} from "@apollo/gateway";

const gateway = new ApolloGateway({
    serviceList: [
        {name: 'users', url: 'http://localhost:5001'},
        {name: 'reviews', url: 'http://localhost:5002'},
        {name: 'products', url: 'http://localhost:5003'},
    ]
})

const server = new ApolloServer({
    gateway,
    subscriptions: false
})

server.listen().then(({url}) => {
    console.log(`Server ready at ${url}`)
})