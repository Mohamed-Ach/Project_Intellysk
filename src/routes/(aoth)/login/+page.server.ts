import { fail, redirect, type Action } from '@sveltejs/kit'
import { loginSchema } from '$lib/zodForms/formSchema'
import type { Actions, PageServerLoad } from './$types'
import { auth } from '$lib/server/lucia'
import { ZodError } from 'zod'

export const load: PageServerLoad = async ({ locals }) => {
    const session = await locals.auth.validate()
    if (session) {
        throw redirect(302, '/dashboard')
    }
}


const login: Action = async ({ request, locals }) => {

    const formData = Object.fromEntries(await request.formData())

    let result

    try {
        result = loginSchema.parse(formData)

    } catch (err) {
        if (err instanceof ZodError) {
            const { fieldErrors: errors } = err.flatten()

            const { password, ...rest } = formData
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
        const key = await auth.useKey('email', result.email, result.password)

        const session = await auth.createSession({
            userId: key.userId,
            attributes: {},
        })
        locals.auth.setSession(session)
    }
    catch (err) {
        console.log("Wrong email or password")
        return fail(400, { error: "l'email ou le mot de passe doit être incorrect, veuillez vérifier les informations saisies" })
    }

    // ** Redirect to dashboard page
    throw redirect(302, '/dashboard')



}


export const actions: Actions = { login }