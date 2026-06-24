import 'package:flutter/material.dart';

class CategoriesScreen extends StatelessWidget {
  const CategoriesScreen({super.key});

  final List<String> categories = const [
    'BLOWER - MISTBLOWER',
    'BRUSH CUTTER - WEED CUTTER',
    'CHAFF CUTTER / SHREDDER',
    'CHAIN SAW',
    'EARTH AUGER',
    'ENGINE',
    'FOGGER ULV & THERMAL',
    'GARDEN TOOLS & SPRAYERS',
    'HARVESTER',
    'HEDGETRIMMER',
    'INTERCULTIVATOR/POWER WEEDER',
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
                color: Colors.grey[200],
                borderRadius: BorderRadius.circular(4),
              ),
              child: const Icon(Icons.precision_manufacturing, color: Colors.grey),
            ),
            title: Text(
              categories[index],
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
