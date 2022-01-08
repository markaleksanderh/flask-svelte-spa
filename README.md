# Flask Svelte Single Page App

Proof of concept full stack Flask and Svelte app running on Docker.

### Run

Before running, the Svelte app needs to be built.
Change directory to `/client` by running `cd server/app/client`. Run `npm install` followed by `npm run build`.
Once that's finished, change directory back to the root by running `cd ../../..`.
Finally, run `docker-compose build` and `docker-compose up`.