# Use an official Node.js image as the base
FROM node:18-alpine AS builder

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the application
RUN npm run build

# Use a lightweight production image for the runtime
FROM node:18-alpine AS runner

# Set the working directory
WORKDIR /app

# Copy only the necessary files from the builder stage
COPY --from=builder /app/next.config.js ./
COPY --from=builder /app/public ./public
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./

# Expose the port that Next.js runs on
EXPOSE 3000

# Start the Next.js app
CMD ["npm", "start"]
