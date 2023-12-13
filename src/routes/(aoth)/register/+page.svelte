<script lang="ts">
	import { applyAction, enhance } from '$app/forms';
	import type { ActionData } from './$types';
	export let form: ActionData;

	const currentYear: number = new Date().getFullYear();

	// ** The EyeSlash component:
	let isEyeSlash: boolean = false;
	let inputType: string = 'password';

	const toggleEyeSlash = () => {
		isEyeSlash = !isEyeSlash;
		inputType = isEyeSlash ? 'text' : 'password';
	};
</script>

<form
	method="POST"
	class="user-data-form mt-60 lg-mt-40"
	use:enhance={() => {
		return async ({ result }) => {
			await applyAction(result);
		};
	}}
>
	<h2>
		Hi, bienvenue
		<br /> Dos!
	</h2>
	<p class="header-info pt-20 pb-20 lg-pt-10 lg-pb-10">
		Vous avez déjà un compte? Connectez-vous <a href="/login">ici</a>
	</p>

	<div class="row">
		<div class="col-12">
			<div class="input-group-meta mb-20">
				<label for="first_name">Prénom*</label>
				<input
					type="text"
					name="first_name"
					placeholder="John"
					class={form?.errors?.first_name ? 'border-error' : ''}
					value={form?.data?.first_name ?? ''}
					required
				/>
				{#if form?.errors?.first_name}
					<span class="label-text-alt text-error">{form?.errors?.first_name[0]}</span>
				{/if}
			</div>
		</div>
		<div class="col-12">
			<div class="input-group-meta mb-20">
				<label for="last_name">Nom*</label>
				<input
					type="text"
					name="last_name"
					class={form?.errors?.last_name ? 'border-error' : ''}
					value={form?.data?.last_name ?? ''}
					placeholder="Doe"
					required
				/>
				{#if form?.errors?.last_name}
					<span class="label-text-alt text-error">{form?.errors?.last_name[0]}</span>
				{/if}
			</div>
		</div>
		<div class="col-12">
			<div class="input-group-meta mb-20">
				<label for="email">Email*</label>
				<input
					type="email"
					name="email"
					placeholder="email@gmail.com"
					class={form?.errors?.email ? 'border-error' : ''}
					value={form?.data?.email ?? ''}
					required
				/>
				{#if form?.errors?.email}
					<span class="label-text-alt text-error">{form?.errors?.email[0]}</span>
				{/if}
			</div>
		</div>
		<div class="col-12">
			<div class="input-group-meta mb-20">
				<label for="password">Mot de passe*</label>
				<input
					type={inputType}
					name="password"
					placeholder="Enter Password"
					class="pass_log_id {form?.errors?.password ? 'border-error' : ''}"
					value=""
					required
				/>
				<span class="placeholder_icon"
					><span class="passVicon {isEyeSlash ? 'eye-slash' : ''}" on:click={toggleEyeSlash}
						><img src="images/icon/icon_40.svg" alt="" /></span
					></span
				>
				{#if form?.errors?.password}
					<span class="label-text-alt text-error">{form?.errors?.password[0]}</span>
				{/if}
			</div>
		</div>
		<div class="col-12">
			<div class="input-group-meta mb-20">
				<label for="passwordConfirm">Confirmer Mot de passe*</label>
				<input
					type={inputType}
					name="passwordConfirm"
					placeholder="Enter Password"
					class="pass_log_id {form?.errors?.passwordConfirm ? 'border-error' : ''}"
					value=""
					required
				/>
				<span class="placeholder_icon"
					><span class="passVicon {isEyeSlash ? 'eye-slash' : ''}" on:click={toggleEyeSlash}
						><img src="images/icon/icon_40.svg" alt="" /></span
					></span
				>
				{#if form?.errors?.passwordConfirm}
					<span class="label-text-alt text-error">{form?.errors?.passwordConfirm[0]}</span>
				{/if}
			</div>
		</div>
		<div class="col-12">
			<div class="agreement-checkbox d-flex justify-content-between align-items-center sm-mt-10">
				<div>
					<input type="checkbox" id="agree_to_policy" name="terms" />
					<label for="agree_to_policy"
						>En cliquant sur « S'inscrire » &nbsp; Vous acceptez les conditions générales et la
						politique de confidentialité.</label
					>
					{#if form?.errors?.terms}
						<span class="label-text-alt text-error">{form?.errors?.terms[0]}</span>
					{/if}
				</div>
			</div>
			<!-- /.agreement-checkbox -->
		</div>
		<div class="col-12">
			<button type="submit" class="btn-eight w-100 mt-50 mb-40 lg-mt-30 lg-mb-30">S'inscrire</button
			>
			<!-- Alerts Messages -->
			{#if form?.error}
				<div class="alert alert-danger alert-dismissible fade show" role="alert">
					<strong>Avertissement!</strong>
					{form.error}
					<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"
					></button>
				</div>
			{/if}
		</div>
		<div class="col-12">
			<p class="text-center copyright-text m0">Copyright @{currentYear} Intellysk.</p>
		</div>
	</div>
</form>
