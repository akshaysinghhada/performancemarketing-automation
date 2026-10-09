"""
Performance Marketing Automation Toolkit
Author: Akshay Singh Hada
Description: Uses Claude API to generate ad copy for Meta and Google Ads.
"""

import os

import anthropic


# Set your API key from Claude Console.
client = anthropic.Anthropic(
	api_key=os.environ.get("ANTHROPIC_API_KEY")
)


def generate_ad_copy(product_name, target_audience, num_variations=5):
	"""Generate high-converting ad headlines using the Claude API.

	Args:
		product_name: Name of the product.
		target_audience: Description of the target audience.
		num_variations: Number of ad variations to generate.

	Returns:
		A list of ad copy headlines.
	"""
	prompt = f"""You are a performance marketing expert. Generate {num_variations}
high-converting ad headlines for:

Product: {product_name}
Target Audience: {target_audience}

Requirements:
- Max 40 characters per headline
- Use emotional triggers
- Include a clear benefit
- Make them scroll-stopping

Return only the headlines, one per line."""

	response = client.messages.create(
		model="claude-sonnet-5",
		max_tokens=500,
		messages=[{"role": "user", "content": prompt}],
	)

	return response.content[0].text.strip().splitlines()


if __name__ == "__main__":
	headlines = generate_ad_copy(
		product_name="Gold Plated Silver Earrings",
		target_audience=(
			"Indian women aged 25-35, fashion-conscious, working professionals"
		),
	)

	print("Generated Ad Copy:")
	for i, headline in enumerate(headlines, 1):
		print(f"{i}. {headline}")