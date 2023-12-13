import { registerSchema } from '$lib/zodForms/formSchema'
import { fail, redirect, type Action } from '@sveltejs/kit'
import type { Actions, PageServerLoad } from './$types'
import { auth } from '$lib/server/lucia'
import { ZodError } from "zod"


export const load: PageServerLoad = async ({ locals }) => {
    const session = await locals.auth.validate()
    if (session) {
        throw redirect(302, '/dashboard')
    }
}

export const actions = {
    default: async ({ request }) => {

        const formData = Object.fromEntries(await request.formData())
        let result

        try {
            result = registerSchema.parse(formData)

        } catch (err) {
            if (err instanceof ZodError) {
                const { fieldErrors: errors } = err.flatten()

                const { password, passwordConfirm, ...rest } = formData
                return {
                    data: rest,
                    errors
                }
            }
            else {
                return fail(500, { error: "Une erreur s'est produite, veuillez réessayer plus tard" })
            }
        }

        try {

            // ** create a new user
            await auth.createUser({
                key: {
                    providerId: "email",
                    providerUserId: result.email,
                    password: result.password,
                },
                attributes: {
                    first_name: result.first_name,
                    last_name: result.last_name,
                    email: result.email,
                }
            })


        }
        catch (err) {
            return fail(400, { error: "Cet utilisateur existe déjà, essayez de vous connecter ou de vous inscrire avec une autre adresse e-mail" })
        }

        throw redirect(302, '/login')

    }

}
// export const actions: Actions = { register }