FROM node:18-alpine AS builder

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

EXPOSE 8080

# Use the "node" user to run the application
USER node

CMD ["npm", "start"]