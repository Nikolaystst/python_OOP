from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    expenses = 250_000
    sponsors = {"Oracle": {1: 1_500_000, 2: 800_000}, "Honda": {8: 20_000, 10: 10_000}}

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        sponsorship = 0
        for sponsor, val in RedBullTeam.sponsors.items():
            for place, prize in val.items():
                if place >= race_pos:
                    sponsorship += prize
                    break

        sponsorship -= RedBullTeam.expenses
        self.budget += sponsorship
        return f"The revenue after the race is {sponsorship}$. Current budget {self.budget}$"
