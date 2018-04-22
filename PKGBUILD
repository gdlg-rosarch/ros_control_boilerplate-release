# Script generated with Bloom
pkgdesc="ROS - Simple simulation interface and template for setting up a hardware interface for ros_control"
url='https://github.com/davetcoleman/ros_control_boilerplate'

pkgname='ros-kinetic-ros-control-boilerplate'
pkgver='0.4.1_0'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('gflags'
'ros-kinetic-actionlib'
'ros-kinetic-catkin'
'ros-kinetic-cmake-modules'
'ros-kinetic-control-msgs'
'ros-kinetic-control-toolbox'
'ros-kinetic-controller-manager'
'ros-kinetic-hardware-interface'
'ros-kinetic-joint-limits-interface'
'ros-kinetic-roscpp'
'ros-kinetic-rosparam-shortcuts'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-trajectory-msgs'
'ros-kinetic-transmission-interface'
'ros-kinetic-urdf'
)

depends=('ros-kinetic-actionlib'
'ros-kinetic-control-msgs'
'ros-kinetic-control-toolbox'
'ros-kinetic-controller-manager'
'ros-kinetic-hardware-interface'
'ros-kinetic-joint-limits-interface'
'ros-kinetic-roscpp'
'ros-kinetic-rosparam-shortcuts'
'ros-kinetic-sensor-msgs'
'ros-kinetic-std-msgs'
'ros-kinetic-trajectory-msgs'
'ros-kinetic-transmission-interface'
'ros-kinetic-urdf'
)

conflicts=()
replaces=()

_dir=ros_control_boilerplate
source=()
md5sums=()

prepare() {
    cp -R $startdir/ros_control_boilerplate $srcdir/ros_control_boilerplate
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

