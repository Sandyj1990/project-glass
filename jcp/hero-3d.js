/**
 * JCP Hero 3D Scene — Interactive Architecture Stack
 * Three.js scene showing the JCP platform layers with 78 channel nodes
 * connecting to the core commerce engine.
 */
(function() {
  'use strict';

  // Wait for Three.js to load
  function init() {
    var container = document.getElementById('jcp-hero-3d');
    if (!container) return;

    var width = container.clientWidth;
    var height = container.clientHeight;

    // Brand colors
    var INK = 0x2a2a26;
    var CORAL = 0xed6f5c;
    var BONE = 0xfaf5ea;
    var PAPER = 0xf5f0e8;
    var WARM = 0xe8dcc8;

    // Scene setup
    var scene = new THREE.Scene();
    scene.background = new THREE.Color(BONE);

    // Camera
    var camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
    camera.position.set(6, 5, 8);
    camera.lookAt(0, 0, 0);

    // Renderer
    var renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    container.appendChild(renderer.domElement);

    // Lights
    var ambientLight = new THREE.AmbientLight(0xffffff, 0.6);
    scene.add(ambientLight);

    var directionalLight = new THREE.DirectionalLight(0xffffff, 0.8);
    directionalLight.position.set(5, 10, 7);
    directionalLight.castShadow = true;
    scene.add(directionalLight);

    var fillLight = new THREE.DirectionalLight(CORAL, 0.15);
    fillLight.position.set(-5, 3, -5);
    scene.add(fillLight);

    // === Platform Layers ===
    var layers = [];
    var layerData = [
      { y: -1.8, label: 'INFRASTRUCTURE', color: INK, opacity: 0.9 },
      { y: -0.6, label: 'DATA LAYER', color: 0x4a4a44, opacity: 0.85 },
      { y: 0.6, label: 'COMMERCE ENGINE', color: CORAL, opacity: 0.9 },
      { y: 1.8, label: 'CHANNELS', color: 0x8b7355, opacity: 0.8 }
    ];

    layerData.forEach(function(data, i) {
      var geometry = new THREE.BoxGeometry(4.5, 0.35, 3);
      var material = new THREE.MeshPhongMaterial({
        color: data.color,
        transparent: true,
        opacity: data.opacity,
        shininess: 30
      });
      var mesh = new THREE.Mesh(geometry, material);
      mesh.position.y = data.y;
      mesh.castShadow = true;
      mesh.receiveShadow = true;
      scene.add(mesh);
      layers.push(mesh);

      // Edge wireframe
      var edges = new THREE.EdgesGeometry(geometry);
      var lineMat = new THREE.LineBasicMaterial({ color: 0xffffff, transparent: true, opacity: 0.3 });
      var wireframe = new THREE.LineSegments(edges, lineMat);
      wireframe.position.copy(mesh.position);
      scene.add(wireframe);
    });

    // === Channel Nodes (floating above the top layer) ===
    var channelNodes = [];
    var channelCount = 24; // Representative subset
    var channelRadius = 2.8;

    for (var i = 0; i < channelCount; i++) {
      var angle = (i / channelCount) * Math.PI * 2;
      var r = channelRadius + (Math.random() - 0.5) * 0.8;
      var x = Math.cos(angle) * r;
      var z = Math.sin(angle) * r;
      var y = 2.8 + Math.random() * 0.8;

      var nodeGeo = new THREE.SphereGeometry(0.08, 12, 12);
      var nodeMat = new THREE.MeshPhongMaterial({
        color: i % 3 === 0 ? CORAL : (i % 3 === 1 ? INK : 0x8b7355),
        emissive: i % 3 === 0 ? CORAL : 0x000000,
        emissiveIntensity: i % 3 === 0 ? 0.3 : 0
      });
      var node = new THREE.Mesh(nodeGeo, nodeMat);
      node.position.set(x, y, z);
      scene.add(node);
      channelNodes.push(node);

      // Connection line from node to top layer
      var points = [
        new THREE.Vector3(x, y, z),
        new THREE.Vector3(x * 0.3, 2.0, z * 0.3)
      ];
      var lineGeo = new THREE.BufferGeometry().setFromPoints(points);
      var lineMat2 = new THREE.LineBasicMaterial({
        color: CORAL,
        transparent: true,
        opacity: 0.25
      });
      var line = new THREE.Line(lineGeo, lineMat2);
      scene.add(line);
    }

    // === Central Core (glowing sphere in the commerce layer) ===
    var coreGeo = new THREE.SphereGeometry(0.4, 32, 32);
    var coreMat = new THREE.MeshPhongMaterial({
      color: CORAL,
      emissive: CORAL,
      emissiveIntensity: 0.5,
      transparent: true,
      opacity: 0.9
    });
    var core = new THREE.Mesh(coreGeo, coreMat);
    core.position.set(0, 0.6, 0);
    scene.add(core);

    // Core glow ring
    var ringGeo = new THREE.RingGeometry(0.5, 0.7, 32);
    var ringMat = new THREE.MeshBasicMaterial({
      color: CORAL,
      transparent: true,
      opacity: 0.2,
      side: THREE.DoubleSide
    });
    var ring = new THREE.Mesh(ringGeo, ringMat);
    ring.position.set(0, 0.6, 0);
    ring.rotation.x = -Math.PI / 2;
    scene.add(ring);

    // === Data Flow Particles ===
    var particleCount = 80;
    var particleGeo = new THREE.BufferGeometry();
    var particlePositions = new Float32Array(particleCount * 3);
    var particleSpeeds = [];

    for (var p = 0; p < particleCount; p++) {
      var pAngle = Math.random() * Math.PI * 2;
      var pR = Math.random() * 2.5;
      particlePositions[p * 3] = Math.cos(pAngle) * pR;
      particlePositions[p * 3 + 1] = -1.8 + Math.random() * 4.5;
      particlePositions[p * 3 + 2] = Math.sin(pAngle) * pR;
      particleSpeeds.push(0.005 + Math.random() * 0.015);
    }

    particleGeo.setAttribute('position', new THREE.BufferAttribute(particlePositions, 3));
    var particleMat = new THREE.PointsMaterial({
      color: CORAL,
      size: 0.04,
      transparent: true,
      opacity: 0.6
    });
    var particles = new THREE.Points(particleGeo, particleMat);
    scene.add(particles);

    // === Mouse interaction ===
    var mouseX = 0, mouseY = 0;
    var targetRotationX = 0, targetRotationY = 0;
    var isDragging = false;
    var previousMouseX = 0, previousMouseY = 0;
    var rotationX = 0, rotationY = 0;

    container.addEventListener('mousemove', function(e) {
      var rect = container.getBoundingClientRect();
      mouseX = ((e.clientX - rect.left) / width - 0.5) * 2;
      mouseY = ((e.clientY - rect.top) / height - 0.5) * 2;

      if (isDragging) {
        var deltaX = e.clientX - previousMouseX;
        var deltaY = e.clientY - previousMouseY;
        rotationY += deltaX * 0.005;
        rotationX += deltaY * 0.003;
        rotationX = Math.max(-0.5, Math.min(0.5, rotationX));
        previousMouseX = e.clientX;
        previousMouseY = e.clientY;
      }
    });

    container.addEventListener('mousedown', function(e) {
      isDragging = true;
      previousMouseX = e.clientX;
      previousMouseY = e.clientY;
      container.style.cursor = 'grabbing';
    });

    container.addEventListener('mouseup', function() {
      isDragging = false;
      container.style.cursor = 'grab';
    });

    container.addEventListener('mouseleave', function() {
      isDragging = false;
      container.style.cursor = 'grab';
    });

    container.style.cursor = 'grab';

    // === Animation Loop ===
    var clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);
      var elapsed = clock.getElapsedTime();

      // Auto-rotation (slow) + mouse influence
      var autoRotation = elapsed * 0.15;
      var totalRotationY = autoRotation + rotationY;

      // Rotate the entire scene group
      scene.rotation.y = totalRotationY;
      scene.rotation.x = rotationX + mouseY * 0.05;

      // Pulse the core
      var pulse = 1 + Math.sin(elapsed * 2) * 0.1;
      core.scale.set(pulse, pulse, pulse);
      coreMat.emissiveIntensity = 0.4 + Math.sin(elapsed * 3) * 0.2;

      // Rotate the ring
      ring.rotation.z = elapsed * 0.5;
      ringMat.opacity = 0.15 + Math.sin(elapsed * 2) * 0.1;

      // Animate particles (flowing upward)
      var positions = particleGeo.attributes.position.array;
      for (var i = 0; i < particleCount; i++) {
        positions[i * 3 + 1] += particleSpeeds[i];
        if (positions[i * 3 + 1] > 3.5) {
          positions[i * 3 + 1] = -1.8;
        }
      }
      particleGeo.attributes.position.needsUpdate = true;

      // Subtle float on channel nodes
      channelNodes.forEach(function(node, idx) {
        node.position.y += Math.sin(elapsed * 1.5 + idx) * 0.001;
      });

      // Layer breathing
      layers.forEach(function(layer, idx) {
        layer.position.y = layerData[idx].y + Math.sin(elapsed * 0.8 + idx * 0.5) * 0.03;
      });

      renderer.render(scene, camera);
    }

    animate();

    // === Resize handler ===
    window.addEventListener('resize', function() {
      width = container.clientWidth;
      height = container.clientHeight;
      camera.aspect = width / height;
      camera.updateProjectionMatrix();
      renderer.setSize(width, height);
    });
  }

  // Load Three.js from CDN if not already loaded
  if (typeof THREE === 'undefined') {
    var script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js';
    script.onload = init;
    document.head.appendChild(script);
  } else {
    init();
  }
})();
