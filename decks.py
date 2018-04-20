from collections import namedtuple

from models import GameVector, Card, Deck


DeckDefinition = namedtuple(
	"DeckDefinition",
	[
		"focus",
		"direction",
		"power",
		"length",
	]
)

def generate_deck(definition):
	focus = definition.focus
	direction = GameVector(*definition.direction)
	power = definition.power
	length = definition.length

	S = focus * power * length // direction.norm

	target = S * direction

	return target


if __name__ == "__main__":
	police = DeckDefinition(
		1,
		(2,3,4),
		5,
		6
	)
	print generate_deck(police)