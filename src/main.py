from datetime import datetime
from ica import SimulatedAnnealing, find_neighboor
from lib.generators import generate_biased_random_solution, generate_random_solution
from lib.print_utils import ShellColors
from lib.string_to_model import get_file_from_args, get_filename_from_args

if __name__ == "__main__":
    print("Executing as main...")

    protein_sequence = get_file_from_args()

    best_model = None

    for _ in range(250):
        model = generate_biased_random_solution(protein_sequence)

        sa = SimulatedAnnealing(
            lambda model: model.get_energy(),
            find_neighboor,
            actual_s=model.clone(),
            star_s=model.clone(),
            max_iter=100
        )

        new_model = sa.run()

        if new_model.get_energy() < model.get_energy():
            model = new_model.clone()

        print("Model energy is...." + str(model.get_energy()))

        if best_model is None:
            best_model = model.clone()

        if model.get_energy() < best_model.get_energy():
            best_model = model.clone()

    best_model.visualize_model()
    print(ShellColors.RESET + str(best_model.get_energy()))
    best_model.save(
        'data/solutions/{}_{}.dat'.format(get_filename_from_args().split('/')[-1].removesuffix('.dat'), datetime.now().strftime('%d-%m-%Y-%H:%M:%S')))
