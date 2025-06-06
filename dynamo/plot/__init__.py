"""Mapping Vector Field of Single Cells
"""

from .cell_cycle import cell_cycle_scores
from .clustering import infomap, leiden, louvain, streamline_clusters
from .connectivity import nneighbors, plot_connectivity
from .dimension_reduction import pca, trimap, tsne, umap
from .dynamics import dynamics, phase_portraits
from .ezplots import (
    SchemeDiverge,
    SchemeDivergeBWR,
    multiplot,
    plot_jacobian_gene,
    plot_V,
    plot_X,
    zscatter,
    zstreamline,
)
from .fate import fate, fate_bias
from .heatmaps import causality, comb_logic, hessian, plot_hill_function, response
from .least_action_path import lap_min_time, least_action
from .markers import bubble
from .networks import arcPlot, circosPlot, circosPlotDeprecated, hivePlot
from .preprocess import (
    basic_stats,
    biplot,
    exp_by_groups,
    feature_genes,
    highest_frac_genes,
    loading,
    show_fraction,
    variance_explained,
)
from .pseudotime import plot_dim_reduced_direct_graph
from .scatters import scatters, scatters_interactive
from .scPotential import show_landscape
from .sctransform import plot_residual_var, sctransform_plot_fit
from .scVectorField import (  # , plot_LIC_gray
    cell_wise_vectors,
    cell_wise_vectors_3d,
    grid_vectors,
    line_integral_conv,
    plot_energy,
    streamline_plot,
)

# spatial data related
from .space import space
from .state_graph import state_graph
from .streamtube import plot_3d_streamtube
from .time_series import (
    jacobian_kinetics,
    kinetic_curves,
    kinetic_heatmap,
    sensitivity_kinetics,
)
from .topography import (
    plot_fixed_points,
    plot_fixed_points_2d,
    plot_flow_field,
    plot_nullclines,
    plot_separatrix,
    plot_traj,
    topography,
    topography_3D,
)

# from .theme import points
from .utils import quiver_autoscaler, save_fig
from .vector_calculus import (
    acceleration,
    curl,
    curvature,
    divergence,
    jacobian,
    jacobian_heatmap,
    sensitivity,
    sensitivity_heatmap,
    speed,
)

from ._trends import (
    trends
)

from .violin_box import violin_box
from ._jacobian import jacobian_on_gene_axis

__all__ = [
    "quiver_autoscaler",
    "save_fig",
    "scatters",
    "scatters_interactive",
    "basic_stats",
    "show_fraction",
    "feature_genes",
    "variance_explained",
    "biplot",
    "loading",
    "exp_by_groups",
    "highest_frac_genes",
    "cell_cycle_scores",
    "bubble",
    "phase_portraits",
    "dynamics",
    "kinetic_curves",
    "kinetic_heatmap",
    "jacobian_kinetics",
    "sensitivity_kinetics",
    "pca",
    "tsne",
    "umap",
    "trimap",
    "nneighbors",
    "plot_connectivity",
    "cell_wise_vectors",
    "cell_wise_vectors_3d",
    "grid_vectors",
    "streamline_plot",
    "line_integral_conv",
    "plot_energy",
    "plot_3d_streamtube",
    "plot_flow_field",
    "plot_fixed_points_2d",
    "plot_fixed_points",
    "plot_nullclines",
    "plot_separatrix",
    "plot_traj",
    "topography",
    "topography_3D",
    "speed",
    "acceleration",
    "curl",
    "divergence",
    "curvature",
    "jacobian",
    "jacobian_heatmap",
    "sensitivity",
    "sensitivity_heatmap",
    "arcPlot",
    "circosPlot",
    "circosPlotDeprecated",
    "hivePlot",
    "fate_bias",
    "fate",
    "state_graph",
    "least_action",
    "lap_min_time",
    "show_landscape",
    "louvain",
    "leiden",
    "infomap",
    "space",
    "zscatter",
    "zstreamline",
    "multiplot",
    "plot_jacobian_gene",
    "plot_V",
    "plot_X",
    "SchemeDiverge",
    "SchemeDivergeBWR",
    "streamline_clusters",
    "response",
    "plot_hill_function",
    "causality",
    "comb_logic",
    "hessian",
    "sctransform_plot_fit",
    "plot_residual_var",
    "plot_dim_reduced_direct_graph",
    "violin_box",
    "trends",
    "jacobian_on_gene_axis",
]


