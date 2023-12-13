<script lang="ts">
	import { onMount } from 'svelte';

	const handleScroll = () => {
		const scrollTop: number = window.scrollY || document.documentElement.scrollTop;
		const scrollButton = document.querySelector<HTMLButtonElement>('button.scroll-top');

		if (!scrollButton) return;

		if (scrollTop > 200) scrollButton.style.display = 'block';
		else scrollButton.style.display = 'none';
	};

	onMount(() => {
		window.addEventListener('scroll', handleScroll);
		return () => {
			window.removeEventListener('scroll', handleScroll);
		};
	});
</script>

<button class="scroll-top" on:click={() => window.scrollTo({ top: 0, behavior: 'smooth' })}>
	<i class="bi bi-arrow-up-short"></i>
</button>
