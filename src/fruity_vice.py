from requests import get


class FruityVice:
	def __init__(self) -> None:
		self.api = "https://www.fruityvice.com/api"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
		}
	
	def get_all_fruits(self) -> dict:
		return get(
			f"{self.api}/fruit/all",
			headers=self.headers).json()
	
	def get_fruid_by_id(self, fruit_id: int) -> dict:
		return get(
			f"{self.api}/fruit/{fruit_id}",
			headers=self.headers).json()
	
	def get_fruit_by_name(self, fruit_name: str) -> dict:
		return get(
			f"{self.api}/fruit/{fruit_name}",
			headers=self.headers).json()
	
	def get_fruit_by_nutrition_value(
			self,
			fruit_name: str,
			minimum: int,
			maximum: int) -> dict:
		return get(
			f"{self.api}/fruit/{fruit_name}?min={minimum}&max={maximum}",
			headers=self.headers).json()

	def get_fruits_by_family(self, family: str) -> dict:
		return get(
			f"{self.api}/fruit/family/{family}",
			headers=self.headers).json()
	
	def get_fruits_by_genus(self, genus: str) -> dict:
		return get(
			f"{self.api}/fruit/genus/{genus}",
			headers=self.headers).json()

	def get_fruits_by_order(self, order: str) -> dict:
		return get(
			f"{self.api}/fruit/order/{order}",
			headers=self.headers).json()
