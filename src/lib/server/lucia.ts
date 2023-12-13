// src/lib/server/lucia.ts
import { lucia } from "lucia";
import { sveltekit } from "lucia/middleware";
import { dev } from "$app/environment";
import { prisma } from "@lucia-auth/adapter-prisma";
import { client } from '$lib/server/prisma'



export const auth = lucia({
    env: dev ? "DEV" : "PROD",

    middleware: sveltekit(),

    adapter: prisma(client),

    getUserAttributes: (databaseUser) => {
        return {
            first_name: databaseUser.first_name,
            last_name: databaseUser.last_name,
            email: databaseUser.email
        }
    }
})


export type Auth = typeof auth
