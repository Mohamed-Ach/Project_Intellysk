// src/lib/prisma.ts
import { PrismaClient } from "@prisma/client"
import { env } from "$env/dynamic/private"

// declare var __prisma: PrismaClient | undefined

const client = new PrismaClient()

// if (env.NODE_ENV === "development" && !__prisma) {
//     __prisma = client
// }

export { client }