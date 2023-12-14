// import adapter from '@sveltejs/adapter-auto';
// import { vitePreprocess } from '@sveltejs/kit/vite';

// const config = {
// 	preprocess: vitePreprocess(),

// 	kit: {
// 		adapter: adapter()
// 	}
// };

// export default config;


// ** This is The adapter-node version for deploying to Vercel:

import { vitePreprocess } from '@sveltejs/kit/vite';
import adapter from '@sveltejs/adapter-node';

export default {
 preprocess: vitePreprocess(),
	kit: {
		adapter: adapter()
	}
};