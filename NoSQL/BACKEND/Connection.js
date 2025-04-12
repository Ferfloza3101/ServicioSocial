import { MongoClient } from "mongodb";

class MongoDbConnection {
    /**
     * @param {*} db
     * @param {*} collection
     */
    constructor(db, collection) {
        this.uri = "mongodb+srv://student:dPgF0sb0ADBUZHCI@clusterunam.6pxlppf.mongodb.net";
        this.db = db;
        this.collection = collection;
        this.client = '';
    }

    /**
     * @returns MongoDb database.collection
     */
    async connect() {
        this.client = new MongoClient(this.uri);
        const database = this.client.db(this.db);
        const collection = database.collection(this.collection);
        return collection;
    }

    /**
     * @param {*} query
     * @returns json
     */
    async find_one(query) {
        let response = '';
        try {
            const collection_data = await this.connect();
            const data_collection = await collection_data.findOne(query);
            console.log("EN CONSULTA");
            response = data_collection;
        } catch (error) {
            console.log(error);
            response = { "message": 'Error al intentar localizar el dato' };
        } finally {
            await this.client.close();
        }
        return response;
    }
}

export { MongoDbConnection };
