FROM node:18-alpine AS builder

# default backend url for cloud deployment
ENV NEXT_PUBLIC_API_BASE_URL="https://pizza-app-backend-1073187497320.us-west4.run.app"

WORKDIR /app

COPY package*.json ./

RUN npm install

# Set proper permissions for node_modules
RUN chown -R node:node /app/node_modules

COPY . .

RUN npm run build

FROM node:18-alpine AS runner

WORKDIR /app

# Copy only the necessary files from the builder stage
COPY --from=builder /app/public ./public
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./
COPY next.config.ts ./

# Set proper permissions for node_modules in the runner stage
RUN chown -R node:node /app/node_modules

EXPOSE 3000

# Use the "node" user to run the application
USER node

CMD ["npm", "start"]
