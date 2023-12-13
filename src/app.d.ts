import type { PrismaClient } from '@prisma/client'

declare global {
	namespace App {
		interface Locals {
			auth: import("lucia").AuthRequest;
		}
	}

	namespace Lucia {
		type Auth = import("$lib/server/lucia").Auth;
		type DatabaseUserAttributes = {
			email: string
			first_name: string
			last_name: string
		}
		type DatabaseSessionAttributes = object
	}
}

export { }