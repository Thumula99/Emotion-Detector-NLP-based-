import React, { useState, useEffect } from 'react';
import { Search, MapPin, AlertTriangle, Heart, TrendingDown, Shield, X, Leaf } from 'lucide-react';

const endangeredAnimals = [
  {
    id: 1,
    name: "Amur Leopard",
    scientificName: "Panthera pardus orientalis",
    status: "Critically Endangered",
    location: "Russia & China",
    population: "~100 individuals",
    image: "https://images.unsplash.com/photo-1614027164847-1b28cfe1df60?w=800&q=80",
    threats: "Habitat loss, poaching, prey depletion",
    description: "The Amur leopard is one of the rarest big cats in the world. Found in the temperate forests of the Russian Far East and northeastern China, these solitary and nocturnal animals face severe threats from habitat fragmentation and illegal wildlife trade."
  },
  {
    id: 2,
    name: "Javan Rhino",
    scientificName: "Rhinoceros sondaicus",
    status: "Critically Endangered",
    location: "Indonesia",
    population: "~76 individuals",
    image: "https://images.unsplash.com/photo-1551532477-a7842bde1e6a?w=800&q=80",
    threats: "Habitat loss, limited range, disease",
    description: "The Javan rhino is one of the most threatened large mammals on Earth. Once widespread across Southeast Asia, the species now survives only in Ujung Kulon National Park in Java, Indonesia. They are extremely rare and shy."
  },
  {
    id: 3,
    name: "Vaquita",
    scientificName: "Phocoena sinus",
    status: "Critically Endangered",
    location: "Gulf of California, Mexico",
    population: "~10 individuals",
    image: "https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=800&q=80",
    threats: "Bycatch in fishing nets, illegal fishing",
    description: "The vaquita is the world's rarest marine mammal. This small porpoise is found only in the northern Gulf of California. Illegal fishing practices, particularly gillnets used for totoaba fish, have devastated their population."
  },
  {
    id: 4,
    name: "Mountain Gorilla",
    scientificName: "Gorilla beringei beringei",
    status: "Endangered",
    location: "Central Africa",
    population: "~1,000 individuals",
    image: "https://images.unsplash.com/photo-1551927336-574c6f45e3e6?w=800&q=80",
    threats: "Habitat loss, poaching, disease",
    description: "Mountain gorillas live in the volcanic mountains of central Africa. Thanks to intensive conservation efforts, their population has been slowly increasing, but they remain vulnerable to habitat encroachment and human-transmitted diseases."
  },
  {
    id: 5,
    name: "Sumatran Elephant",
    scientificName: "Elephas maximus sumatranus",
    status: "Critically Endangered",
    location: "Sumatra, Indonesia",
    population: "~2,400 individuals",
    image: "https://images.unsplash.com/photo-1564760055775-d63b17a55c44?w=800&q=80",
    threats: "Deforestation, human-elephant conflict",
    description: "The Sumatran elephant has lost nearly 70% of its habitat in just one generation due to palm oil plantations and agricultural expansion. Human-elephant conflict continues to threaten their survival."
  },
  {
    id: 6,
    name: "Hawksbill Turtle",
    scientificName: "Eretmochelys imbricata",
    status: "Critically Endangered",
    location: "Tropical oceans worldwide",
    population: "Unknown, severely depleted",
    image: "https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=800&q=80",
    threats: "Shell trade, habitat loss, climate change",
    description: "Hawksbill turtles are named for their narrow, pointed beak. They play a crucial role in marine ecosystems by controlling sponge populations on coral reefs. Their beautiful shells have made them targets for illegal wildlife trade."
  },
  {
    id: 7,
    name: "Saola",
    scientificName: "Pseudoryx nghetinhensis",
    status: "Critically Endangered",
    location: "Vietnam & Laos",
    population: "Unknown, extremely rare",
    image: "https://images.unsplash.com/photo-1551532477-a7842bde1e6a?w=800&q=80",
    threats: "Hunting, habitat loss",
    description: "Known as the 'Asian Unicorn,' the saola was only discovered in 1992. So rare that it's almost never seen in the wild, this forest-dwelling bovine is threatened by snares set for other animals and habitat destruction."
  },
  {
    id: 8,
    name: "Sumatran Orangutan",
    scientificName: "Pongo abelii",
    status: "Critically Endangered",
    location: "Sumatra, Indonesia",
    population: "~14,000 individuals",
    image: "https://images.unsplash.com/photo-1540573133985-87b6da6d54a9?w=800&q=80",
    threats: "Deforestation, illegal pet trade",
    description: "Sumatran orangutans are found only in the northern part of Sumatra. These highly intelligent primates spend most of their lives in trees and are losing their forest homes at an alarming rate to logging and agricultural development."
  }
];

const statusColors = {
  "Critically Endangered": "bg-gradient-to-r from-red-500 to-red-600 text-white",
  "Endangered": "bg-gradient-to-r from-orange-500 to-orange-600 text-white"
};

export default function EndangeredAnimalsBlog() {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedAnimal, setSelectedAnimal] = useState(null);
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    setIsVisible(true);
  }, []);

  const filteredAnimals = endangeredAnimals.filter(animal =>
    animal.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    animal.location.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="min-h-screen bg-gradient-to-br from-green-50 via-white to-green-100">
      {/* Animated Background */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-20 left-20 w-96 h-96 bg-green-300 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-pulse"></div>
        <div className="absolute top-40 right-20 w-96 h-96 bg-emerald-300 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-pulse" style={{animationDelay: '1s'}}></div>
        <div className="absolute bottom-20 left-1/2 w-96 h-96 bg-teal-300 rounded-full mix-blend-multiply filter blur-3xl opacity-30 animate-pulse" style={{animationDelay: '2s'}}></div>
      </div>

      {/* Hero Header */}
      <header className={`relative backdrop-blur-md bg-white/80 border-b-4 border-green-500 shadow-xl transition-all duration-1000 ${isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 -translate-y-10'}`}>
        <div className="max-w-7xl mx-auto px-4 py-16">
          <div className="flex items-center justify-center gap-4 mb-4">
            <div className="relative">
              <Leaf className="w-16 h-16 text-green-600 animate-pulse" />
              <div className="absolute inset-0 bg-green-500 blur-xl opacity-50 animate-pulse"></div>
            </div>
            <h1 className="text-6xl font-black text-transparent bg-clip-text bg-gradient-to-r from-green-600 via-emerald-500 to-teal-600">
              ENDANGERED SPECIES
            </h1>
          </div>
          <p className="text-center text-xl text-gray-700 max-w-2xl mx-auto leading-relaxed font-medium">
            Protecting our planet's precious wildlife. Every species deserves a future.
          </p>
          <div className="flex items-center justify-center gap-8 mt-8">
            <div className="text-center bg-white/60 backdrop-blur-sm rounded-2xl px-8 py-4 shadow-lg border-2 border-green-200">
              <div className="text-3xl font-bold text-green-600">41,000+</div>
              <div className="text-sm text-gray-600 font-medium">Species Threatened</div>
            </div>
            <div className="h-12 w-px bg-green-300"></div>
            <div className="text-center bg-white/60 backdrop-blur-sm rounded-2xl px-8 py-4 shadow-lg border-2 border-green-200">
              <div className="text-3xl font-bold text-emerald-600">16,000+</div>
              <div className="text-sm text-gray-600 font-medium">Near Extinction</div>
            </div>
          </div>
        </div>
      </header>

      <div className="relative max-w-7xl mx-auto px-4 py-12">
        {/* Search Bar */}
        <div className={`mb-12 transition-all duration-1000 delay-300 ${isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'}`}>
          <div className="relative max-w-2xl mx-auto">
            <Search className="absolute left-5 top-1/2 transform -translate-y-1/2 w-6 h-6 text-green-600" />
            <input
              type="text"
              placeholder="Search endangered species..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="w-full pl-16 pr-6 py-5 rounded-2xl bg-white backdrop-blur-lg border-4 border-green-400 text-gray-800 placeholder-gray-500 focus:outline-none focus:ring-4 focus:ring-green-300 focus:border-green-500 transition-all text-lg shadow-xl"
            />
          </div>
        </div>

        {/* Alert Banner */}
        <div className={`backdrop-blur-md bg-gradient-to-r from-green-400/30 to-emerald-400/30 border-4 border-green-500 rounded-2xl p-6 mb-12 shadow-xl transition-all duration-1000 delay-500 ${isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'}`}>
          <div className="flex items-start gap-4">
            <Shield className="w-8 h-8 text-green-700 flex-shrink-0 mt-1" />
            <div>
              <h3 className="text-xl font-bold text-green-900 mb-2">About the IUCN Red List</h3>
              <p className="text-gray-800 leading-relaxed font-medium">
                The world's most comprehensive inventory of the global conservation status of biological species. 
                This data represents decades of scientific research and conservation efforts worldwide.
              </p>
            </div>
          </div>
        </div>

        {/* Animal Cards Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {filteredAnimals.map((animal, index) => (
            <div
              key={animal.id}
              className={`group relative backdrop-blur-md bg-white rounded-3xl overflow-hidden border-4 border-green-300 hover:border-green-500 transition-all duration-500 hover:scale-105 hover:shadow-2xl hover:shadow-green-500/30 cursor-pointer ${isVisible ? 'opacity-100 translate-y-0' : 'opacity-0 translate-y-10'}`}
              style={{transitionDelay: `${700 + index * 100}ms`}}
              onClick={() => setSelectedAnimal(animal)}
            >
              {/* Image */}
              <div className="relative h-64 overflow-hidden">
                <img 
                  src={animal.image} 
                  alt={animal.name}
                  className="w-full h-full object-cover transition-transform duration-700 group-hover:scale-110"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-green-900/80 via-green-900/20 to-transparent"></div>
                <div className={`absolute top-4 right-4 px-4 py-2 rounded-full text-xs font-bold ${statusColors[animal.status]} shadow-lg backdrop-blur-sm`}>
                  {animal.status}
                </div>
              </div>

              {/* Content */}
              <div className="p-6 bg-gradient-to-b from-white to-green-50">
                <h3 className="text-2xl font-bold text-gray-900 mb-2 group-hover:text-green-700 transition-colors">
                  {animal.name}
                </h3>
                <p className="text-sm italic text-gray-600 mb-4">{animal.scientificName}</p>
                
                <div className="flex items-center gap-2 text-sm text-gray-700 mb-3 font-medium">
                  <MapPin className="w-4 h-4 text-green-600" />
                  <span>{animal.location}</span>
                </div>
                
                <div className="flex items-center gap-2 text-sm mb-4">
                  <TrendingDown className="w-4 h-4 text-red-600" />
                  <span className="text-gray-700">Population: <strong className="text-gray-900">{animal.population}</strong></span>
                </div>
                
                <p className="text-sm text-gray-600 line-clamp-3 leading-relaxed mb-4">
                  {animal.description}
                </p>
                
                <div className="flex items-center justify-between pt-4 border-t-2 border-green-200">
                  <span className="text-green-600 font-bold group-hover:text-green-700 transition-colors">
                    Learn More →
                  </span>
                  <Heart className="w-5 h-5 text-gray-400 group-hover:text-red-500 group-hover:fill-red-500 transition-all" />
                </div>
              </div>

              {/* Glow Effect */}
              <div className="absolute inset-0 bg-gradient-to-t from-green-500/0 to-green-500/0 group-hover:from-green-500/10 group-hover:to-transparent transition-all duration-500 pointer-events-none"></div>
            </div>
          ))}
        </div>

        {filteredAnimals.length === 0 && (
          <div className="text-center py-20">
            <div className="text-6xl mb-4">🔍</div>
            <p className="text-gray-600 text-xl font-medium">No species found matching your search.</p>
          </div>
        )}
      </div>

      {/* Modal */}
      {selectedAnimal && (
        <div 
          className="fixed inset-0 bg-black/60 backdrop-blur-xl flex items-center justify-center p-4 z-50 animate-in fade-in duration-300"
          onClick={() => setSelectedAnimal(null)}
        >
          <div 
            className="bg-white rounded-3xl max-w-4xl w-full max-h-[90vh] overflow-y-auto border-4 border-green-500 shadow-2xl animate-in zoom-in duration-300"
            onClick={(e) => e.stopPropagation()}
          >
            {/* Modal Image */}
            <div className="relative h-96 overflow-hidden">
              <img 
                src={selectedAnimal.image} 
                alt={selectedAnimal.name}
                className="w-full h-full object-cover"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-white via-green-900/50 to-transparent"></div>
              
              <button
                onClick={() => setSelectedAnimal(null)}
                className="absolute top-6 right-6 w-12 h-12 rounded-full bg-white/90 backdrop-blur-md border-2 border-green-500 flex items-center justify-center text-green-700 hover:bg-white transition-all hover:scale-110 shadow-xl"
              >
                <X className="w-6 h-6" />
              </button>

              <div className="absolute bottom-6 left-6 right-6">
                <h2 className="text-5xl font-black text-white mb-2 drop-shadow-2xl">
                  {selectedAnimal.name}
                </h2>
                <p className="text-xl italic text-green-100 drop-shadow-lg">{selectedAnimal.scientificName}</p>
              </div>
            </div>

            {/* Modal Content */}
            <div className="p-8 bg-gradient-to-b from-white to-green-50">
              <div className={`inline-block px-6 py-3 rounded-full text-sm font-bold ${statusColors[selectedAnimal.status]} shadow-lg mb-6`}>
                {selectedAnimal.status}
              </div>
              
              <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                <div className="backdrop-blur-md bg-green-100 border-4 border-green-300 rounded-2xl p-6 shadow-lg">
                  <MapPin className="w-8 h-8 text-green-700 mb-3" />
                  <h4 className="font-bold text-gray-900 mb-2 text-lg">Location</h4>
                  <p className="text-gray-700 font-medium">{selectedAnimal.location}</p>
                </div>
                <div className="backdrop-blur-md bg-green-100 border-4 border-green-300 rounded-2xl p-6 shadow-lg">
                  <TrendingDown className="w-8 h-8 text-red-600 mb-3" />
                  <h4 className="font-bold text-gray-900 mb-2 text-lg">Population</h4>
                  <p className="text-gray-700 font-medium">{selectedAnimal.population}</p>
                </div>
                <div className="backdrop-blur-md bg-green-100 border-4 border-green-300 rounded-2xl p-6 shadow-lg">
                  <AlertTriangle className="w-8 h-8 text-orange-600 mb-3" />
                  <h4 className="font-bold text-gray-900 mb-2 text-lg">Status</h4>
                  <p className="text-gray-700 font-medium">Critical</p>
                </div>
              </div>
              
              <div className="mb-8">
                <h4 className="text-2xl font-bold text-gray-900 mb-4 flex items-center gap-2">
                  <Leaf className="w-6 h-6 text-green-600" />
                  About This Species
                </h4>
                <p className="text-gray-700 leading-relaxed text-lg font-medium">{selectedAnimal.description}</p>
              </div>
              
              <div className="mb-8 backdrop-blur-md bg-red-50 border-4 border-red-300 rounded-2xl p-6 shadow-lg">
                <h4 className="text-2xl font-bold text-gray-900 mb-4 flex items-center gap-3">
                  <AlertTriangle className="w-6 h-6 text-red-600" />
                  Major Threats
                </h4>
                <p className="text-gray-700 text-lg font-medium">{selectedAnimal.threats}</p>
              </div>
              
              <div className="flex gap-4">
                <button
                  onClick={() => setSelectedAnimal(null)}
                  className="flex-1 bg-gray-100 hover:bg-gray-200 border-4 border-gray-300 text-gray-800 font-bold py-4 px-6 rounded-xl transition-all hover:scale-105 shadow-lg"
                >
                  Close
                </button>
                <button className="flex-1 bg-gradient-to-r from-green-500 to-emerald-600 hover:from-green-600 hover:to-emerald-700 text-white font-bold py-4 px-6 rounded-xl transition-all hover:scale-105 flex items-center justify-center gap-3 shadow-xl border-4 border-green-600">
                  <Heart className="w-6 h-6" />
                  Support Conservation
                </button>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Footer */}
      <footer className="relative backdrop-blur-md bg-white/80 border-t-4 border-green-500 mt-20 py-12 shadow-xl">
        <div className="max-w-7xl mx-auto px-4 text-center">
          <div className="flex items-center justify-center gap-3 mb-4">
            <Leaf className="w-10 h-10 text-green-600 animate-pulse" />
          </div>
          <p className="text-xl text-gray-800 mb-3 font-bold">Every species matters. Every action counts.</p>
          <p className="text-sm text-gray-600 font-medium">Data sourced from the IUCN Red List of Threatened Species</p>
          <p className="text-xs text-gray-500 mt-4">© 2024 Endangered Species Alert. Together for conservation.</p>
        </div>
      </footer>
    </div>
  );
}