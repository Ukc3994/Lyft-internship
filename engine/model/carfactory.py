class CarFactory:
    def __init__(self):
        self.tire_wear = None

    def set_tire_wear(self, tire_wear):
        self.tire_wear = tire_wear

    def needs_tire_service(self):
      if self.tire_wear is None:
        raise ValueError("Tire wear information is missing")

    # Carrigan tires should be serviced if any tire wear value is >= 0.9
      if isinstance(self.tire_wear, list):
        if any(wear >= 0.9 for wear in self.tire_wear):
            return True

    # Octoprime tires should be serviced if the sum of all tire wear values is >= 3
      if isinstance(self.tire_wear, list):
        if sum(self.tire_wear) >= 3:
            return True

    return False

