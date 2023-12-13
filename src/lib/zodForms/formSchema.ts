import { z } from "zod"

export const registerSchema = z
    .object({
        first_name: z
            .string({ required_error: "Le prénom est requis!" })
            .min(3, { message: "Le prénom doit comporter au moins 3 caractères!" })
            .max(60, { message: "Le prénom doit comporter moins de 60 caractères!" })
            .trim()
            .refine(value => /^[a-zA-Z]+$/.test(value), { message: "Le prénom ne peut contenir que des lettres!" }),

        last_name: z
            .string({ required_error: "Le nom est requis!" })
            .min(3, { message: "Le nom doit comporter au moins 3 caractères!" })
            .max(60, { message: "Le nom doit comporter moins de 60 caractères!" })
            .trim()
            .refine(value => /^[a-zA-Z]+$/.test(value), { message: "Le nom ne peut contenir que des lettres!" }),


        email: z
            .string({ required_error: "L'e-mail est requis" })
            .min(5, { message: "Le nom doit comporter au moins 5 caractères!" })
            .max(70, { message: "L'e-mail doit contenir moins de 70 caractères" })
            .email({ message: "l'e-mail doit être une adresse e-mail valide" }),


        password: z
            .string({ required_error: "Mot de passe requis" })
            .min(8, { message: "Mot de passe doit être d'au moins 8 caractères" })
            .max(120, { message: "Le mot de passe doit contenir moins de 120 caractères" })
            .trim()
            .refine(value => /\d/.test(value), { message: "le mot de passe doit contenir au moins un chiffre" })
            .refine(value => /[!@#$%^&*(),.?":{}|<>]/.test(value), { message: "Le mot de passe doit contenir au moins un caractère spécial" }),

        passwordConfirm: z
            .string({ required_error: "Mot de passe requis" })
            .min(8, { message: "Mot de passe doit être d'au moins 8 caractères" })
            .max(120, { message: "Le mot de passe doit contenir moins de 120 caractères" })
            .trim()
            .refine(value => /\d/.test(value), { message: "le mot de passe doit contenir au moins un chiffre" })
            .refine(value => /[!@#$%^&*(),.?":{}|<>]/.test(value), { message: "Le mot de passe doit contenir au moins un caractère spécial" }),



        terms: z.enum(["on"], { required_error: "Vous devez accepter les termes et conditions d' Intellysk" })
    })
    .superRefine(({ passwordConfirm, password }, ctx) => {
        if (passwordConfirm !== password) {
            ctx.addIssue({
                code: "custom",
                message: "Les champs Mot de passe et Confirmer le mot de passe doivent correspondre",
                path: ["password"]
            })
            ctx.addIssue({
                code: "custom",
                message: "Les champs Mot de passe et Confirmer le mot de passe doivent correspondre",
                path: ["passwordConfirm"]
            })
        }
    })


export const loginSchema = z
    .object({
        email: z
            .string({ required_error: "L'e-mail est requis" })
            .min(5, { message: "Le nom doit comporter au moins 5 caractères!" })
            .max(70, { message: "L'e-mail doit contenir moins de 70 caractères" })
            .email({ message: "l'e-mail doit être une adresse e-mail valide" }),

        password: z
            .string({ required_error: "Mot de passe requis" })
            .trim()

    })