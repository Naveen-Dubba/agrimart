import 'package:flutter/material.dart';

class CategoriesScreen extends StatelessWidget {
  const CategoriesScreen({super.key});

  final List<Map<String, String>> categories = const [
    {'name': 'BLOWER - MISTBLOWER', 'image': 'assets/images/cat_sprayer.png'},
    {'name': 'BRUSH CUTTER - WEED CUTTER', 'image': 'assets/images/cat_chainsaw.png'},
    {'name': 'CHAFF CUTTER / SHREDDER', 'image': 'assets/images/cat_engine.png'},
    {'name': 'CHAIN SAW', 'image': 'assets/images/cat_chainsaw.png'},
    {'name': 'EARTH AUGER', 'image': 'assets/images/cat_engine.png'},
    {'name': 'ENGINE', 'image': 'assets/images/cat_engine.png'},
    {'name': 'FOGGER ULV & THERMAL', 'image': 'assets/images/cat_sprayer.png'},
    {'name': 'GARDEN TOOLS & SPRAYERS', 'image': 'assets/images/cat_sprayer.png'},
    {'name': 'HARVESTER', 'image': 'assets/images/cat_chainsaw.png'},
    {'name': 'HEDGETRIMMER', 'image': 'assets/images/cat_chainsaw.png'},
    {'name': 'INTERCULTIVATOR/POWER WEEDER', 'image': 'assets/images/cat_engine.png'},
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: const Icon(Icons.arrow_back),
          onPressed: () {},
        ),
        title: const Text('Categories'),
      ),
      body: ListView.separated(
        itemCount: categories.length,
        separatorBuilder: (context, index) => const Divider(height: 1),
        itemBuilder: (context, index) {
          return ListTile(
            leading: Container(
              width: 50,
              height: 50,
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(4),
              ),
              child: Image.asset(
                categories[index]['image']!,
                fit: BoxFit.contain,
              ),
            ),
            title: Text(
              categories[index]['name']!,
              style: const TextStyle(
                fontWeight: FontWeight.w500,
                fontSize: 14,
                color: Color(0xFF424242),
              ),
            ),
            trailing: const Icon(Icons.add, color: Color(0xFF43A047)),
            onTap: () {},
          );
        },
      ),
    );
  }
}
